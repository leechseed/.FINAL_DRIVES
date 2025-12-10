import pg8000.native

# 1. DATABASE CONNECTION
DB_CONFIG = {
    "database": "atomic_astro_db",  
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1",  # <--- I kept your password here
    "host": "localhost",
    "port": 5433
}

# 2. THE CHARACTER DATA (Updated with Demographics)
new_char = {
    "name": "The Lunar Queen",
    "archetype": "Mother / Cancer Archetype",
    "level": 5,
    "age": 29,                  # <--- NEW FIELD
    "sex": "Female",            # <--- NEW FIELD
    "race": "Human",            # <--- NEW FIELD
    "ethnicity": "Lunar-Isles", # <--- NEW FIELD
    "description": "A test character representing pure Lunar energy."
}

# 3. THE ASTROLOGY DATA
# Using Moon variables since this is a Lunar character
char_values = {
    "MOON_NEED_CORE": "To feel emotionally safe and needed by her family.",
    "MOON_EMOTIONAL_STYLE": "Fluctuating, absorbent, protective, nurturing.",
    "MOON_TRIGGER_SET": "Rejection, coldness, threats to the home.",
    "MOON_ATTACHMENT_PATTERN": "Anxious-Preoccupied (Clings tight).",
    "MOON_SURVIVAL_SCRIPT": "Retreat into the shell and harden the outer walls."
}

def create_character():
    try:
        conn = pg8000.native.Connection(**DB_CONFIG)
        print("✅ Connected to database!")

        # 1. Create the Character Row (Now includes Age, Sex, Race, Ethnicity)
        print(f"--> Creating Character: {new_char['name']}")
        result = conn.run("""
            INSERT INTO characters (name, archetype, level, age, sex, race, ethnicity, description)
            VALUES (:name, :arch, :lvl, :age, :sex, :race, :eth, :desc)
            RETURNING char_id;
        """, 
        name=new_char['name'], 
        arch=new_char['archetype'], 
        lvl=new_char['level'], 
        age=new_char['age'], 
        sex=new_char['sex'], 
        race=new_char['race'], 
        eth=new_char['ethnicity'], 
        desc=new_char['description']
        )
        
        char_id = result[0][0]
        print(f"   -> Character ID created: {char_id}")

        # 2. Look up Variable IDs
        print("--> Looking up Variable IDs...")
        var_map = {}
        rows = conn.run("SELECT var_code, atomic_var_id FROM atomic_variable_def")
        for row in rows:
            var_map[row[0]] = row[1]

        # 3. Insert the Atomic Values
        print("--> Saving Atomic Values...")
        count = 0
        for code, value_text in char_values.items():
            var_id = var_map.get(code)
            
            if var_id:
                conn.run("""
                    INSERT INTO atomic_values (char_id, atomic_var_id, value_text)
                    VALUES (:cid, :vid, :val);
                """, cid=char_id, vid=var_id, val=value_text)
                count += 1
            else:
                print(f"   ⚠️ Warning: Variable '{code}' not found in DB definitions.")

        conn.close()
        print(f"\n🎉 SUCCESS! Created '{new_char['name']}' with {count} data points.")

    except Exception as e:
        print("\n❌ ERROR:", e)

if __name__ == "__main__":
    create_character()