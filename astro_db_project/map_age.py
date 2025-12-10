import pg8000.native

DB_CONFIG = {
    "database": "atomic_astro_db",  
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1", 
    "host": "localhost",
    "port": 5433
}

# THE SPIRAL AGE WIRING PLAN
# Logic derived from your "Relationship" and "Personal" Focus columns
wiring_plan = [
    # --- PHASE 1: THE LEARNING LOOP ---
    
    # CHILDHOOD (1-12) - Focus: Familial / Morality
    {"source": "AGE_CHILDHOOD", "target": "POLITENESS", "weight": 2.0},      # Learning the rules
    {"source": "AGE_CHILDHOOD", "target": "COMPASSION", "weight": 1.5},      # Attachment bonding
    {"source": "AGE_CHILDHOOD", "target": "ASSERTIVENESS", "weight": -1.0},  # Dependent status

    # ADOLESCENCE (12-18) - Focus: Platonic / Affinity
    {"source": "AGE_ADOLESCENCE", "target": "ENTHUSIASM", "weight": 2.0},    # Finding the tribe
    {"source": "AGE_ADOLESCENCE", "target": "VOLATILITY", "weight": 1.5},    # High hormonal flux
    {"source": "AGE_ADOLESCENCE", "target": "OPENNESS_CREATIVE", "weight": 1.5}, # Identity formation

    # PILGRIM (18-24) - Focus: Sexual / Social
    {"source": "AGE_PILGRIM", "target": "ENTHUSIASM", "weight": 1.5},        # Social exploration
    {"source": "AGE_PILGRIM", "target": "ASSERTIVENESS", "weight": 1.0},     # Sexual agency
    {"source": "AGE_PILGRIM", "target": "OPENNESS_CREATIVE", "weight": 1.5}, # Experiencing the world

    # --- PHASE 2: THE HARDENING LOOP ---

    # ADULTHOOD (24-30) - Focus: Systematic / Ego-Centric (Saturn Phase)
    {"source": "AGE_ADULTHOOD", "target": "INDUSTRIOUSNESS", "weight": 2.0}, # Career building
    {"source": "AGE_ADULTHOOD", "target": "ASSERTIVENESS", "weight": 1.5},   # Ego assertion
    {"source": "AGE_ADULTHOOD", "target": "ORDERLINESS", "weight": 1.0},     # Learning systems

    # CLASSIFICATION (30-36) - Focus: Contractual / ID-Centric
    {"source": "AGE_CLASSIFICATION", "target": "ORDERLINESS", "weight": 2.0}, # Contracts & Mortgages
    {"source": "AGE_CLASSIFICATION", "target": "INTELLECT", "weight": 1.5},   # Defining the specific Self
    {"source": "AGE_CLASSIFICATION", "target": "VOLATILITY", "weight": -1.0}, # Settling down

    # --- PHASE 3: THE MASTERY LOOP ---

    # REVISITATION (36-42) - Focus: Familial / Morality II (Mid-Life)
    {"source": "AGE_REVISITATION", "target": "COMPASSION", "weight": 1.5},    # Parenting / Caretaking
    {"source": "AGE_REVISITATION", "target": "VOLATILITY", "weight": 1.0},    # The Crisis window
    {"source": "AGE_REVISITATION", "target": "INTELLECT", "weight": 1.0},     # Re-evaluating ethics

    # ASCENSION (42-48) - Focus: Platonic / Affinity II
    {"source": "AGE_ASCENTION", "target": "OPENNESS_CREATIVE", "weight": 1.5},# Refined tastes/Arts
    {"source": "AGE_ASCENTION", "target": "ENTHUSIASM", "weight": 1.0},       # Selective socializing
    {"source": "AGE_ASCENTION", "target": "INDUSTRIOUSNESS", "weight": 1.0},  # Peak executive power

    # MASTERY (48-54) - Focus: Sexual / Social II
    {"source": "AGE_MASTERY", "target": "ASSERTIVENESS", "weight": 2.0},      # Leadership / Command
    {"source": "AGE_MASTERY", "target": "ENTHUSIASM", "weight": 1.0},        # Second wind of life force
    {"source": "AGE_MASTERY", "target": "INTELLECT", "weight": 1.5},         # Strategic mastery

    # ELDER (54+) - Focus: Familial / Morality III
    {"source": "AGE_ELDER", "target": "ORDERLINESS", "weight": 1.5},          # Conserving tradition
    {"source": "AGE_ELDER", "target": "VOLATILITY", "weight": -2.0},          # High emotional regulation
    {"source": "AGE_ELDER", "target": "POLITENESS", "weight": 1.5}            # Role of the Sage
]

def wire_age():
    try:
        conn = pg8000.native.Connection(**DB_CONFIG)
        print("✅ Connected. Wiring Spiral Age Logic...")

        var_map = {row[0]: row[1] for row in conn.run("SELECT var_code, atomic_var_id FROM atomic_variable_def")}
        dim_map = {row[0]: row[1] for row in conn.run("SELECT dimension_code, dimension_id FROM overlay_model_dimension")}

        count = 0
        for wire in wiring_plan:
            src_id = var_map.get(wire['source'])
            tgt_id = dim_map.get(wire['target'])
            
            if src_id and tgt_id:
                conn.run("""
                    INSERT INTO variable_mappings (atomic_var_id, dimension_id, weight)
                    VALUES (:vid, :did, :w)
                    ON CONFLICT (atomic_var_id, dimension_id) DO UPDATE SET weight = :w;
                """, vid=src_id, did=tgt_id, w=wire['weight'])
                count += 1
                print(f"   🔗 Wired: {wire['source']} -> {wire['target']}")
            else:
                 print(f"   ⚠️ Skipping: {wire['source']}")

        conn.close()
        print(f"\n🎉 SUCCESS! Age logic wired.")

    except Exception as e:
        print("\n❌ ERROR:", e)

if __name__ == "__main__":
    wire_age()