import pg8000.native

# --- IMPORT YOUR WIRING SCRIPTS ---
import map_bfas         # Core Astrology -> Psychology
import map_heritage     # Race/Culture -> Psychology
import map_age          # Age Spiral -> Psychology
# import map_goon_phys  <-- REMOVED

DB_CONFIG = {
    "database": "atomic_astro_db",  
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1", 
    "host": "localhost",
    "port": 5433
}

def refresh_all_logic():
    """
    The Master Switch.
    Runs every logic script you have installed.
    """
    try:
        conn = pg8000.native.Connection(**DB_CONFIG)
        print("\n⚙️  SYSTEM: Refreshing Logic Layer...")

        # 1. RUN THE WIRING SCRIPTS (The Cables)
        print("   [1/3] Wiring Astrology -> BFAS...")
        map_bfas.wire_bfas()
        
        print("   [2/3] Wiring Heritage -> BFAS...")
        map_heritage.wire_heritage()
        
        print("   [3/3] Wiring Age -> BFAS...")
        map_age.wire_age()

        # 2. RUN AGE ASSIGNMENTS (The Spiral)
        print("   [4/4] Calculating Age Spirals...")
        ranges = [
            (1, 12, "AGE_CHILDHOOD"), (12, 18, "AGE_ADOLESCENCE"),
            (18, 24, "AGE_PILGRIM"), (24, 30, "AGE_ADULTHOOD"),
            (30, 36, "AGE_CLASSIFICATION"), (36, 42, "AGE_REVISITATION"),
            (42, 48, "AGE_ASCENTION"), (48, 54, "AGE_MASTERY"),
            (54, 150, "AGE_ELDER")
        ]
        
        var_map = {row[0]: row[1] for row in conn.run("SELECT var_code, atomic_var_id FROM atomic_variable_def")}
        
        # Clear old assignments to prevent duplicates
        conn.run("DELETE FROM atomic_values WHERE value_text = 'Spiral Auto-Assign'")

        for min_a, max_a, code in ranges:
            target_id = var_map.get(code)
            if target_id:
                conn.run("""
                    INSERT INTO atomic_values (char_id, atomic_var_id, value_text)
                    SELECT char_id, :vid, 'Spiral Auto-Assign'
                    FROM characters 
                    WHERE age >= :min_a AND age < :max_a
                """, vid=target_id, min_a=min_a, max_a=max_a)

        conn.close()
        print("✅ SYSTEM: All Systems synced. The engine is hot.\n")

    except Exception as e:
        print(f"❌ SYSTEM ERROR: {e}")