import pg8000.native

DB_CONFIG = {
    "database": "atomic_astro_db",  
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1", 
    "host": "localhost",
    "port": 5433
}

def seed_phenotype():
    try:
        conn = pg8000.native.Connection(**DB_CONFIG)
        print("✅ Connected. Building Phenotype System...")

        # 1. Ensure Domain Exists (The Fix)
        # We insert it first to make sure it exists, avoiding the crash.
        print("--> Checking/Creating HERITAGE Domain...")
        conn.run("INSERT INTO domains (domain_code, name) VALUES ('HERITAGE', 'Race & Ethnicity') ON CONFLICT (domain_code) DO NOTHING")
        
        # Now we can safely grab the ID
        dom_id = conn.run("SELECT domain_id FROM domains WHERE domain_code = 'HERITAGE'")[0][0]

        # 2. Create Subsystem
        print("--> Creating Phenotype Subsystem...")
        conn.run("""
            INSERT INTO subsystems (domain_id, subsystem_code, name) 
            VALUES (:did, 'PHENOTYPE', 'Physical Appearance')
            ON CONFLICT (subsystem_code) DO NOTHING
        """, did=dom_id)
        
        sub_id = conn.run("SELECT subsystem_id FROM subsystems WHERE subsystem_code = 'PHENOTYPE'")[0][0]

        # 3. Define the Variables
        vars_data = [
            {"code": "PHENO_SKIN", "name": "Skin Complexion", "desc": "The tone, undertone, and texture of the skin."},
            {"code": "PHENO_HAIR", "name": "Hair Texture/Color", "desc": "The structure and color of the hair."},
            {"code": "PHENO_EYES", "name": "Eye Color/Shape", "desc": "The color and shape of the eyes."},
            {"code": "PHENO_BUILD", "name": "Body Type", "desc": "The skeletal and muscular frame."}
        ]

        # 4. Insert Variables
        print("--> Seeding Variables...")
        for v in vars_data:
            conn.run("""
                INSERT INTO atomic_variable_def (subsystem_id, var_code, name, description)
                VALUES (:sid, :code, :name, :desc)
                ON CONFLICT (var_code) DO NOTHING;
            """, sid=sub_id, code=v['code'], name=v['name'], desc=v['desc'])

        conn.close()
        print("\n🎉 SUCCESS! Phenotype System installed.")

    except Exception as e:
        print("\n❌ ERROR:", e)

if __name__ == "__main__":
    seed_phenotype()