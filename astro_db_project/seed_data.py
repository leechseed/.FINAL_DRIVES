import pg8000.native

# 1. DATABASE CONNECTION CONFIG
# We are using pg8000 now - it's pure Python (no DLL errors!)
DB_CONFIG = {
    "database": "atomic_astro_db",  
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1",  # <--- UPDATE THIS!
    "host": "localhost",
    "port": 5433
}

# 2. THE DATA (Domains & Subsystems)
domains_data = [
    {
        "code": "CORE_IDENTITY",
        "name": "Core Identity System",
        "subsystems": [
            {"code": "SUN", "name": "Sun Identity"},
            {"code": "MOON", "name": "Moon Emotion"},
            {"code": "ASC", "name": "Ascendant / Persona"},
            {"code": "CHART_SHAPE", "name": "Chart Shape & Patterns"}
        ]
    },
    {
        "code": "PLANETARY", 
        "name": "Planetary Subsystems",
        "subsystems": [
            {"code": "MERCURY", "name": "Mercury Mind"},
            {"code": "VENUS", "name": "Venus Love/Values"},
            {"code": "MARS", "name": "Mars Action/Drive"},
            {"code": "JUPITER", "name": "Jupiter Growth"},
            {"code": "SATURN", "name": "Saturn Structure"},
            {"code": "URANUS", "name": "Uranus Change"},
            {"code": "NEPTUNE", "name": "Neptune Dreams"},
            {"code": "PLUTO", "name": "Pluto Power/Transform"}
        ]
    },
    {
        "code": "POINTS",
        "name": "Points & Nodes",
        "subsystems": [
            {"code": "NORTH_NODE", "name": "North Node Destiny"},
            {"code": "SOUTH_NODE", "name": "South Node Karma"},
            {"code": "MC", "name": "Midheaven Career"},
            {"code": "IC", "name": "Imum Coeli Roots"},
            {"code": "CHIRON", "name": "Chiron Wound"},
            {"code": "POF", "name": "Part of Fortune"}
        ]
    },
    {
        "code": "HOUSES",
        "name": "Life Domains (Houses)",
        "subsystems": [
            {"code": "H1", "name": "House 1 (Self)"},
            {"code": "H2", "name": "House 2 (Resources)"},
            {"code": "H3", "name": "House 3 (Comm)"},
            {"code": "H4", "name": "House 4 (Home)"},
            {"code": "H5", "name": "House 5 (Creativity)"},
            {"code": "H6", "name": "House 6 (Routine)"},
            {"code": "H7", "name": "House 7 (Partners)"},
            {"code": "H8", "name": "House 8 (Transformation)"},
            {"code": "H9", "name": "House 9 (Belief)"},
            {"code": "H10", "name": "House 10 (Status)"},
            {"code": "H11", "name": "House 11 (Community)"},
            {"code": "H12", "name": "House 12 (Unconscious)"}
        ]
    }
]

def seed_database():
    try:
        # Connect to DB using pg8000
        conn = pg8000.native.Connection(**DB_CONFIG)
        print("✅ Connected to database!")

        # Loop through data and insert
        for domain in domains_data:
            print(f"--> Inserting Domain: {domain['name']}")
            
            # Insert Domain (and safely ignore duplicates)
            # pg8000 uses :param syntax for variables, not %s
            result = conn.run("""
                INSERT INTO domains (domain_code, name) 
                VALUES (:code, :name) 
                ON CONFLICT (domain_code) DO NOTHING
                RETURNING domain_id;
            """, code=domain['code'], name=domain['name'])
            
            # If we inserted a new one, result is a list of rows. If duplicate, it's empty.
            if len(result) > 0:
                domain_id = result[0][0]
            else:
                # If it already existed, we need to look it up
                lookup = conn.run("SELECT domain_id FROM domains WHERE domain_code = :code", code=domain['code'])
                domain_id = lookup[0][0]

            # Insert Subsystems
            for sub in domain['subsystems']:
                conn.run("""
                    INSERT INTO subsystems (domain_id, subsystem_code, name)
                    VALUES (:did, :code, :name)
                    ON CONFLICT (subsystem_code) DO NOTHING;
                """, did=domain_id, code=sub['code'], name=sub['name'])
        
        # pg8000 auto-commits by default, but we close nicely
        conn.close()
        print("\n🎉 SUCCESS! Database seeded with Domains and Subsystems.")

    except Exception as e:
        print("\n❌ ERROR:", e)

if __name__ == "__main__":
    seed_database()