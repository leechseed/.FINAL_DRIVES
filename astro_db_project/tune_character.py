import pg8000.native

DB_CONFIG = {
    "database": "atomic_astro_db",
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1",
    "host": "localhost",
    "port": 5433
}

def set_resonance(char_name, planet, volume, reason="Manual Adjustment"):
    try:
        conn = pg8000.native.Connection(**DB_CONFIG)
        
        # 1. Get Character ID
        res = conn.run("SELECT char_id FROM characters WHERE name = :n", n=char_name)
        if not res:
            print(f"❌ Error: Character '{char_name}' not found.")
            return
        cid = res[0][0]

        # 2. Validate Input
        planet = planet.upper()
        if volume < 0 or volume > 12:
            print("❌ Error: Volume must be between 0 and 12.")
            return

        # 3. Upsert the Resonance (Update if exists, Insert if new)
        print(f"🎛️  Tuning {char_name}: Setting {planet} to Volume {volume}...")
        conn.run("""
            INSERT INTO character_resonance (char_id, subsystem_code, volume, narrative_reason)
            VALUES (:cid, :sub, :vol, :reas)
            ON CONFLICT (char_id, subsystem_code) 
            DO UPDATE SET volume = :vol, narrative_reason = :reas
        """, cid=cid, sub=planet, vol=volume, reas=reason)

        conn.close()
        print("✅ Success. Character psychology updated.")

    except Exception as e:
        print("\n❌ ERROR:", e)

if __name__ == "__main__":
    # --- MANUAL TEST AREA ---
    # You can change these values to test different settings
    set_resonance("The Lunar Queen", "MOON", 12, "Trauma Response: Maximum Evangelion")
    set_resonance("The Lunar Queen", "SUN", 4, "Identity is suppressed by the Moon.")