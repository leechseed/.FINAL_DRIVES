import pg8000.native

DB_CONFIG = {
    "database": "atomic_astro_db",
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1",
    "host": "localhost",
    "port": 5433
}

def init_mappings():
    try:
        conn = pg8000.native.Connection(**DB_CONFIG)
        print("⚙️  Initializing Mapping Architecture...")

        # 1. Drop it if it exists (Start Fresh)
        conn.run("DROP TABLE IF EXISTS bfas_mapping")

        # 2. Create the Table
        # This is the "Cable Management" table that connects Text to Math.
        conn.run("""
            CREATE TABLE bfas_mapping (
                map_id SERIAL PRIMARY KEY,
                source_value VARCHAR(100),  -- e.g. "CULT_CANCER" or "Sun in Aries"
                target_trait VARCHAR(50),   -- e.g. "Withdrawal"
                weight FLOAT,               -- e.g. 1.0 or -0.5
                source_type VARCHAR(50),    -- e.g. "ASTRO", "CULTURE", "AGE"
                UNIQUE(source_value, target_trait)
            );
        """)

        print("✅ SUCCESS: 'bfas_mapping' table created.")
        conn.close()

    except Exception as e:
        print(f"❌ ERROR: {e}")

if __name__ == "__main__":
    init_mappings()