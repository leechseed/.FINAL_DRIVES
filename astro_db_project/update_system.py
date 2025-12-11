import pg8000.native
import archetype_text  # Reads your new master file

DB_CONFIG = {
    "database": "atomic_astro_db",  
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1", 
    "host": "localhost",
    "port": 5433
}

def update_system():
    try:
        conn = pg8000.native.Connection(**DB_CONFIG)
        print("✅ Connected. Initiating System Update...")

        # --- 1. SEED PLANETARY CONTEXT (The Blurbs) ---
        print("\n[1/3] Seeding Narrative Context...")
        conn.run("""
            CREATE TABLE IF NOT EXISTS narrative_definitions (
                definition_id SERIAL PRIMARY KEY,
                context_code VARCHAR(50) UNIQUE NOT NULL,
                title VARCHAR(100),
                description TEXT
            );
        """)
        
        for code, data in archetype_text.PLANETARY_CONTEXT.items():
            conn.run("""
                INSERT INTO narrative_definitions (context_code, title, description)
                VALUES (:code, :title, :desc)
                ON CONFLICT (context_code) DO UPDATE 
                SET title = :title, description = :desc
            """, code=code, title=data['title'], desc=data['desc'])
        print("   -> Context updated.")

        # --- 2. ENSURE SUBSYSTEMS EXIST ---
        print("\n[2/3] Verifying Subsystems...")
        # We need a domain for the Psychology
        conn.run("INSERT INTO domains (domain_code, name) VALUES ('PSYCHE', 'Psychological Profile') ON CONFLICT (domain_code) DO NOTHING")
        dom_id = conn.run("SELECT domain_id FROM domains WHERE domain_code = 'PSYCHE'")[0][0]

        # Map prefixes to Subsystem Names
        subsystems = {
            "SUN": "Solar Identity", "MOON": "Lunar Emotional Core", 
            "MERCURY": "Mercury Mind", "VENUS": "Venusian Desire", 
            "MARS": "Martian Conflict", "JUPITER": "Jupiterian Belief",
            "SATURN": "Saturnian Debt", "URANUS": "Uranian Chaos",
            "NEPTUNE": "Neptunian Illusion", "PLUTO": "Plutonic Power",
            "SN": "Karmic Node", "CHIRON": "Core Wound"
        }

        sub_ids = {}
        for code, name in subsystems.items():
            conn.run("""
                INSERT INTO subsystems (domain_id, subsystem_code, name) 
                VALUES (:did, :code, :name) ON CONFLICT (subsystem_code) DO NOTHING
            """, did=dom_id, code=code, name=name)
            sub_ids[code] = conn.run("SELECT subsystem_id FROM subsystems WHERE subsystem_code = :c", c=code)[0][0]

        # --- 3. AUTO-REGISTER VARIABLES ---
        print("\n[3/3] Registering New Variables from Library...")
        # We use 'ARIES' as the template to find all possible keys
        template_keys = archetype_text.ZODIAC_DATA['ARIES']['lore'].keys()
        
        new_count = 0
        for var_code in template_keys:
            # Determine which subsystem it belongs to based on prefix
            prefix = var_code.split('_')[0]
            sid = sub_ids.get(prefix, sub_ids.get("SUN")) # Default to Sun if unknown

            # Insert Definition
            conn.run("""
                INSERT INTO atomic_variable_def (subsystem_id, var_code, name, description)
                VALUES (:sid, :code, :name, 'Narrative Variable')
                ON CONFLICT (var_code) DO NOTHING
            """, sid=sid, code=var_code, name=var_code.replace('_', ' ').title())
            new_count += 1
            
        print(f"   -> Scanned {new_count} variables. Database is synced.")
        
        conn.close()
        print("\n🎉 SYSTEM READY. You can now generate characters.")

    except Exception as e:
        print("\n❌ ERROR:", e)

if __name__ == "__main__":
    update_system()