import pg8000.native

DB_CONFIG = {
    "database": "atomic_astro_db",  
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1", 
    "host": "localhost",
    "port": 5433
}

# 1. THE DEFINITIONS (Your Spiral Model)
spiral_ages = [
    {"code": "AGE_CHILDHOOD", "name": "Childhood (1-12)", "desc": "Focus: Familial / Morality."},
    {"code": "AGE_ADOLESCENCE", "name": "Adolescence (12-18)", "desc": "Focus: Platonic / Affinity."},
    {"code": "AGE_PILGRIM", "name": "Pilgrim (18-24)", "desc": "Focus: Sexual / Social."},
    {"code": "AGE_ADULTHOOD", "name": "Adulthood (24-30)", "desc": "Focus: Systematic / Ego-Centric."},
    {"code": "AGE_CLASSIFICATION", "name": "Classification (30-36)", "desc": "Focus: Contractual / ID-Centric."},
    {"code": "AGE_REVISITATION", "name": "Revisitation (36-42)", "desc": "Focus: Familial / Morality (II)."},
    {"code": "AGE_ASCENTION", "name": "Ascention (42-48)", "desc": "Focus: Platonic / Affinity (II)."},
    {"code": "AGE_MASTERY", "name": "Mastery (48-54)", "desc": "Focus: Sexual / Social (II)."},
    {"code": "AGE_ELDER", "name": "Elder (54+)", "desc": "Focus: Familial / Morality (III)."}
]

# 2. THE WIRING (Connecting Age -> BFAS)
wiring_plan = [
    # CHILDHOOD
    {"source": "AGE_CHILDHOOD", "target": "POLITENESS", "weight": 2.0},
    {"source": "AGE_CHILDHOOD", "target": "COMPASSION", "weight": 1.5},
    {"source": "AGE_CHILDHOOD", "target": "ASSERTIVENESS", "weight": -1.0},
    # ADOLESCENCE
    {"source": "AGE_ADOLESCENCE", "target": "ENTHUSIASM", "weight": 2.0},
    {"source": "AGE_ADOLESCENCE", "target": "VOLATILITY", "weight": 1.5},
    {"source": "AGE_ADOLESCENCE", "target": "OPENNESS_CREATIVE", "weight": 1.5},
    # PILGRIM
    {"source": "AGE_PILGRIM", "target": "ENTHUSIASM", "weight": 1.5},
    {"source": "AGE_PILGRIM", "target": "ASSERTIVENESS", "weight": 1.0},
    {"source": "AGE_PILGRIM", "target": "OPENNESS_CREATIVE", "weight": 1.5},
    # ADULTHOOD
    {"source": "AGE_ADULTHOOD", "target": "INDUSTRIOUSNESS", "weight": 2.0},
    {"source": "AGE_ADULTHOOD", "target": "ASSERTIVENESS", "weight": 1.5},
    {"source": "AGE_ADULTHOOD", "target": "ORDERLINESS", "weight": 1.0},
    # CLASSIFICATION
    {"source": "AGE_CLASSIFICATION", "target": "ORDERLINESS", "weight": 2.0},
    {"source": "AGE_CLASSIFICATION", "target": "INTELLECT", "weight": 1.5},
    {"source": "AGE_CLASSIFICATION", "target": "VOLATILITY", "weight": -1.0},
    # REVISITATION
    {"source": "AGE_REVISITATION", "target": "COMPASSION", "weight": 1.5},
    {"source": "AGE_REVISITATION", "target": "VOLATILITY", "weight": 1.0},
    # ASCENTION
    {"source": "AGE_ASCENTION", "target": "OPENNESS_CREATIVE", "weight": 1.5},
    {"source": "AGE_ASCENTION", "target": "INDUSTRIOUSNESS", "weight": 1.0},
    # MASTERY
    {"source": "AGE_MASTERY", "target": "ASSERTIVENESS", "weight": 2.0},
    {"source": "AGE_MASTERY", "target": "INTELLECT", "weight": 1.5},
    # ELDER
    {"source": "AGE_ELDER", "target": "ORDERLINESS", "weight": 1.5},
    {"source": "AGE_ELDER", "target": "VOLATILITY", "weight": -2.0},
    {"source": "AGE_ELDER", "target": "POLITENESS", "weight": 1.5}
]

def run_fix():
    try:
        conn = pg8000.native.Connection(**DB_CONFIG)
        print("✅ Connected. Starting Master Age Fix...")

        # --- A. SETUP DOMAIN & SUBSYSTEM ---
        print("--> Ensuring Age Domain exists...")
        conn.run("INSERT INTO domains (domain_code, name) VALUES ('DEMOG', 'Demographics') ON CONFLICT (domain_code) DO NOTHING")
        dom_id = conn.run("SELECT domain_id FROM domains WHERE domain_code = 'DEMOG'")[0][0]
        
        conn.run("INSERT INTO subsystems (domain_id, subsystem_code, name) VALUES (:did, 'AGE_SPIRAL', 'Spiral Age Archetypes') ON CONFLICT (subsystem_code) DO NOTHING", did=dom_id)
        sub_id = conn.run("SELECT subsystem_id FROM subsystems WHERE subsystem_code = 'AGE_SPIRAL'")[0][0]

        # --- B.0 SAFETY WIPE (FIX FOR ERROR 23503) ---
        print("--> Safety: Removing old assignments from characters first...")
        conn.run("""
            DELETE FROM atomic_values 
            WHERE atomic_var_id IN (
                SELECT atomic_var_id FROM atomic_variable_def WHERE subsystem_id = :sid
            )
        """, sid=sub_id)

        # --- B. SEED VARIABLES ---
        print("--> Seeding 9 Spiral Variables...")
        conn.run("DELETE FROM atomic_variable_def WHERE subsystem_id = :sid", sid=sub_id)
        
        for var in spiral_ages:
            conn.run("""
                INSERT INTO atomic_variable_def (subsystem_id, var_code, name, description)
                VALUES (:sid, :code, :name, :desc)
            """, sid=sub_id, code=var['code'], name=var['name'], desc=var['desc'])

        # --- C. WIRE TO COMPILER ---
        print("--> Wiring Age -> BFAS...")
        # Get Maps
        var_map = {row[0]: row[1] for row in conn.run("SELECT var_code, atomic_var_id FROM atomic_variable_def")}
        dim_map = {row[0]: row[1] for row in conn.run("SELECT dimension_code, dimension_id FROM overlay_model_dimension")}

        for wire in wiring_plan:
            src_id = var_map.get(wire['source'])
            tgt_id = dim_map.get(wire['target'])
            if src_id and tgt_id:
                conn.run("""
                    INSERT INTO variable_mappings (atomic_var_id, dimension_id, weight)
                    VALUES (:vid, :did, :w)
                    ON CONFLICT (atomic_var_id, dimension_id) DO UPDATE SET weight = :w;
                """, vid=src_id, did=tgt_id, w=wire['weight'])

        # --- D. ASSIGN TO CHARACTERS ---
        print("--> Auto-Assigning Age Archetypes to Characters...")
        
        # 2. Assign based on Ranges (The Logic)
        ranges = [
            (1, 12, "AGE_CHILDHOOD"),
            (12, 18, "AGE_ADOLESCENCE"),
            (18, 24, "AGE_PILGRIM"),
            (24, 30, "AGE_ADULTHOOD"),
            (30, 36, "AGE_CLASSIFICATION"),
            (36, 42, "AGE_REVISITATION"),
            (42, 48, "AGE_ASCENTION"),
            (48, 54, "AGE_MASTERY"),
            (54, 150, "AGE_ELDER")
        ]

        for min_a, max_a, code in ranges:
            target_var_id = var_map.get(code)
            if target_var_id:
                conn.run("""
                    INSERT INTO atomic_values (char_id, atomic_var_id, value_text)
                    SELECT char_id, :vid, 'Spiral Auto-Assign'
                    FROM characters 
                    WHERE age >= :min_a AND age < :max_a
                """, vid=target_var_id, min_a=min_a, max_a=max_a)
                print(f"   -> Assigned {code} to characters aged {min_a}-{max_a}")

        conn.close()
        print("\n🎉 SUCCESS! Age System completely rebuilt and assigned.")

    except Exception as e:
        print("\n❌ ERROR:", e)

if __name__ == "__main__":
    run_fix()