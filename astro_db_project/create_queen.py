import pg8000.native
import astro_logic      # The Brain
import archetype_text   # The Library

DB_CONFIG = {
    "database": "atomic_astro_db",  
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1", 
    "host": "localhost",
    "port": 5433
}

# --- SETTINGS ---
CHAR_NAME = "The Lunar Queen"
ARCHETYPE = "CANCER" # Must match a key in ZODIAC_DATA
LEVEL = 50
AGE = 28 # Age Phase: Adulthood (Saturn Return approaching)

def create_character():
    try:
        conn = pg8000.native.Connection(**DB_CONFIG)
        print(f"✅ Connected. Birthing {CHAR_NAME}...")

        # 1. Load Data
        data = archetype_text.ZODIAC_DATA[ARCHETYPE]
        lore = data['lore']

        # 2. Create/Update Character
        exist = conn.run("SELECT char_id FROM characters WHERE name = :n", n=CHAR_NAME)
        if exist:
            cid = exist[0][0]
            print("   -> Updating existing entity.")
            conn.run("DELETE FROM atomic_values WHERE char_id = :cid", cid=cid) # Wipe clean
            conn.run("""
                UPDATE characters SET archetype=:arch, level=:lvl, age=:age, 
                ethnicity=:eth, description=:desc 
                WHERE char_id=:cid
            """, cid=cid, arch=f"Matriarch / {ARCHETYPE}", lvl=LEVEL, age=AGE, 
               eth=data['culture_code'], desc=data['description'])
        else:
            print("   -> Creating new entity.")
            cid = conn.run("""
                INSERT INTO characters (name, archetype, level, age, ethnicity, description)
                VALUES (:name, :arch, :lvl, :age, :eth, :desc)
                RETURNING char_id
            """, name=CHAR_NAME, arch=f"Matriarch / {ARCHETYPE}", lvl=LEVEL, age=AGE,
               eth=data['culture_code'], desc=data['description'])[0][0]

        # 3. Insert All Lore (Sun, Moon, Mars, Pluto...)
        print("   -> Injecting Psychology...")
        var_map = {row[0]: row[1] for row in conn.run("SELECT var_code, atomic_var_id FROM atomic_variable_def")}
        
        for code, text in lore.items():
            vid = var_map.get(code)
            if vid:
                conn.run("INSERT INTO atomic_values (char_id, atomic_var_id, value_text) VALUES (:cid, :vid, :val)", 
                         cid=cid, vid=vid, val=text)

        # 4. Insert Cultural Flag
        cult_id = var_map.get(data['culture_code'])
        if cult_id:
             conn.run("INSERT INTO atomic_values (char_id, atomic_var_id, value_text) VALUES (:cid, :vid, 'Dominant Trait')", cid=cid, vid=cult_id)

        conn.close()
        
        # 5. Run The Logic Engine
        astro_logic.refresh_all_logic()
        print(f"🎉 SUCCESS! {CHAR_NAME} is alive.")

    except Exception as e:
        print("\n❌ ERROR:", e)

if __name__ == "__main__":
    create_character()