import pg8000.native

DB_CONFIG = {
    "database": "atomic_astro_db",  
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1", 
    "host": "localhost",
    "port": 5433
}

def seed_heritage():
    try:
        conn = pg8000.native.Connection(**DB_CONFIG)
        print("✅ Connected. Building Heritage System...")

        # 1. Ensure Domain Exists
        conn.run("INSERT INTO domains (domain_code, name) VALUES ('HERITAGE', 'Race & Ethnicity') ON CONFLICT (domain_code) DO NOTHING")
        dom_id = conn.run("SELECT domain_id FROM domains WHERE domain_code = 'HERITAGE'")[0][0]

        # 2. Ensure Subsystems Exist
        conn.run("INSERT INTO subsystems (domain_id, subsystem_code, name) VALUES (:did, 'RACE_BIO', 'Biological Form (Elements)') ON CONFLICT (subsystem_code) DO NOTHING", did=dom_id)
        bio_id = conn.run("SELECT subsystem_id FROM subsystems WHERE subsystem_code = 'RACE_BIO'")[0][0]

        conn.run("INSERT INTO subsystems (domain_id, subsystem_code, name) VALUES (:did, 'ETHNIC_CULTURE', 'Cultural Root (Zodiac)') ON CONFLICT (subsystem_code) DO NOTHING", did=dom_id)
        cult_id = conn.run("SELECT subsystem_id FROM subsystems WHERE subsystem_code = 'ETHNIC_CULTURE'")[0][0]

        # 3. Define Variables (THESE MUST MATCH map_heritage.py EXACTLY)
        races = [
            {"code": "RACE_FIRE", "name": "Fire-Kin"},
            {"code": "RACE_EARTH", "name": "Earth-Kin"},
            {"code": "RACE_AIR", "name": "Air-Kin"},
            {"code": "RACE_WATER", "name": "Water-Kin"}
        ]

        cultures = [
            {"code": "CULT_ARIES", "name": "The Vanguard (Aries)"},
            {"code": "CULT_TAURUS", "name": "The Builders (Taurus)"},
            {"code": "CULT_GEMINI", "name": "The Weavers (Gemini)"},
            {"code": "CULT_CANCER", "name": "The Hearth (Cancer)"},
            {"code": "CULT_LEO", "name": "The Regents (Leo)"},
            {"code": "CULT_VIRGO", "name": "The Architects (Virgo)"},
            {"code": "CULT_LIBRA", "name": "The Diplomats (Libra)"},
            {"code": "CULT_SCORPIO", "name": "The Deep (Scorpio)"},
            {"code": "CULT_SAGITTARIUS", "name": "The Voyagers (Sagittarius)"},
            {"code": "CULT_CAPRICORN", "name": "The Elders (Capricorn)"},
            {"code": "CULT_AQUARIUS", "name": "The Exiles (Aquarius)"},
            {"code": "CULT_PISCES", "name": "The Mystics (Pisces)"}
        ]

        # 4. Insert Variables
        print("--> Seeding Variables...")
        for r in races:
            conn.run("""
                INSERT INTO atomic_variable_def (subsystem_id, var_code, name, description) 
                VALUES (:sid, :code, :name, 'Elemental Race Trait') 
                ON CONFLICT (var_code) DO NOTHING
            """, sid=bio_id, code=r['code'], name=r['name'])
        
        for c in cultures:
            conn.run("""
                INSERT INTO atomic_variable_def (subsystem_id, var_code, name, description) 
                VALUES (:sid, :code, :name, 'Zodiac Culture Trait') 
                ON CONFLICT (var_code) DO NOTHING
            """, sid=cult_id, code=c['code'], name=c['name'])

        conn.close()
        print("\n🎉 SUCCESS! Heritage variables seeded.")

    except Exception as e:
        print("\n❌ ERROR:", e)

if __name__ == "__main__":
    seed_heritage()