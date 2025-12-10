import pg8000.native

DB_CONFIG = {
    "database": "atomic_astro_db",  
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1", 
    "host": "localhost",
    "port": 5433
}

def seed_age_logic():
    try:
        conn = pg8000.native.Connection(**DB_CONFIG)
        print("✅ Connected. Building The Spiral Age System...")

        # 1. Ensure Domain Exists
        conn.run("INSERT INTO domains (domain_code, name) VALUES ('DEMOG', 'Demographics') ON CONFLICT (domain_code) DO NOTHING")
        dom_id = conn.run("SELECT domain_id FROM domains WHERE domain_code = 'DEMOG'")[0][0]

        # 2. Create Subsystem
        conn.run("INSERT INTO subsystems (domain_id, subsystem_code, name) VALUES (:did, 'AGE_SPIRAL', 'Spiral Age Archetypes') ON CONFLICT (subsystem_code) DO NOTHING", did=dom_id)
        sub_id = conn.run("SELECT subsystem_id FROM subsystems WHERE subsystem_code = 'AGE_SPIRAL'")[0][0]

        # 3. Your Spiral Archetypes
        # I included your "Focus" notes in the description so the AI context knows about them.
        spiral_ages = [
            {"code": "AGE_CHILDHOOD", "name": "Childhood (1-12)", "desc": "Focus: Familial / Morality. Learning the rules of the clan."},
            {"code": "AGE_ADOLESCENCE", "name": "Adolescence (12-18)", "desc": "Focus: Platonic / Affinity. Finding the tribe and personal tastes."},
            {"code": "AGE_PILGRIM", "name": "Pilgrim (18-24)", "desc": "Focus: Sexual / Social. Leaving the nest, exploring desire and society."},
            {"code": "AGE_ADULTHOOD", "name": "Adulthood (24-30)", "desc": "Focus: Systematic / Ego-Centric. Climbing hierarchies and building the Self."},
            {"code": "AGE_CLASSIFICATION", "name": "Classification (30-36)", "desc": "Focus: Contractual / ID-Centric. Binding contracts, defining the core identity."},
            {"code": "AGE_REVISITATION", "name": "Revisitation (36-42)", "desc": "Focus: Familial / Morality (II). The Mid-Life re-evaluation of roots and ethics."},
            {"code": "AGE_ASCENTION", "name": "Ascention (42-48)", "desc": "Focus: Platonic / Affinity (II). Higher-level connection and refined tastes."},
            {"code": "AGE_MASTERY", "name": "Mastery (48-54)", "desc": "Focus: Sexual / Social (II). Generative power and social leadership."},
            {"code": "AGE_ELDER", "name": "Elder (54+)", "desc": "Focus: Familial / Morality (III). The Patriarch/Matriarch legacy role."}
        ]

        # 4. Clear old variables (Safety wipe)
        print("--> Cleaning up old Age Archetypes...")
        conn.run("DELETE FROM atomic_variable_def WHERE subsystem_id = :sid", sid=sub_id)

        # 5. Insert New Spiral
        for var in spiral_ages:
            conn.run("""
                INSERT INTO atomic_variable_def (subsystem_id, var_code, name, description)
                VALUES (:sid, :code, :name, :desc)
                ON CONFLICT (var_code) DO NOTHING;
            """, sid=sub_id, code=var['code'], name=var['name'], desc=var['desc'])
            print(f"   -> Added Spiral Phase: {var['name']}")

        conn.close()
        print("\n🎉 SUCCESS! The Spiral Age System is installed.")

    except Exception as e:
        print("\n❌ ERROR:", e)

if __name__ == "__main__":
    seed_age_logic()