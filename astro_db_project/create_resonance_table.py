import pg8000.native

DB_CONFIG = {
    "database": "atomic_astro_db",  
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1", 
    "host": "localhost",
    "port": 5433
}

def create_resonance_table():
    try:
        conn = pg8000.native.Connection(**DB_CONFIG)
        print("✅ Connected. Creating Resonance Mixing Board...")

        # 1. Create the Table
        # "volume" is the 1-12 integer setting for that planet/subsystem
        conn.run("""
            CREATE TABLE IF NOT EXISTS character_resonance (
                resonance_id SERIAL PRIMARY KEY,
                char_id INT REFERENCES characters(char_id) ON DELETE CASCADE,
                subsystem_code VARCHAR(50), 
                volume INT CHECK (volume BETWEEN 0 AND 12), -- The 1-12 Dial
                narrative_reason TEXT,
                UNIQUE (char_id, subsystem_code)
            );
        """)

        print("🎉 SUCCESS! 'character_resonance' table created.")
        conn.close()

    except Exception as e:
        print("\n❌ ERROR:", e)

if __name__ == "__main__":
    create_resonance_table()