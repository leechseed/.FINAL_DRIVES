import pg8000.native
import astro_logic  # Imports the brain to auto-calculate stats

DB_CONFIG = {
    "database": "atomic_astro_db",  
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1", 
    "host": "localhost",
    "port": 5433
}

# 1. CHARACTER BASICS
king_data = {
    "name": "The Solar King",
    "archetype": "Ruler / Leo Archetype",
    "level": 10,
    "age": 34,                  # Phase: Classification
    "sex": "Male",
    "race": "Fire-Kin",         # Narrative Header
    "ethnicity": "Solar-Regent",# Narrative Header
    "description": "The absolute center of gravity. A ruler who burns to provide."
}

# 2. THE FULL LORE (All Planets)
text_values = {
    # --- SUN (Identity) ---
    "SUN_IDENTITY_AXIS": "I am the Center who holds the structure together.",
    "SUN_MOTIVATION_VECTOR": "To bring order and visibility to the chaos.",
    "SUN_EGO_STYLE": "Radiant, demanding, magnanimous, proud.",
    "SUN_THEMATIC_QUESTION": "What happens when the light goes out?",
    "SUN_PRIDE_CENTER": "His ability to provide for and protect his subjects.",

    # --- MOON (Emotional Core - New!) ---
    "MOON_NEED_CORE": "To be admired and reflected by those he loves.",
    "MOON_EMOTIONAL_STYLE": "Warm, generous, but easily wounded by indifference.",
    "MOON_TRIGGER_SET": "Being ignored or treated as ordinary.",
    "MOON_ATTACHMENT_PATTERN": "Secure-Dominant (Provides safety, demands loyalty).",
    "MOON_SURVIVAL_SCRIPT": "Increase the volume/brightness until seen.",

    # --- MERCURY (Mind - New!) ---
    "MERCURY_COGNITION_STYLE": "Intuitive and declarative. He speaks in decrees.",
    "MERCURY_DECISION_PROCESS": "Decisive, based on honor rather than data.",
    "MERCURY_COMMUNICATION_STYLE": "Oratorical, dramatic, authoritative.",
    "MERCURY_SOCIAL_INTELLIGENCE_PROFILE": "High charisma, low subtlety. Misses subtext.",

    # --- VENUS (Values/Love - New!) ---
    "VENUS_LOVE_STYLE": "Grand gestures. Love is a public performance.",
    "VENUS_ATTRACTION_PROFILE": "Attracted to beauty, loyalty, and those who let him lead.",
    "VENUS_RELATIONAL_VALUES": "Loyalty, aesthetics, and public respect.",
    "VENUS_PLEASURE_METRICS": "Feasts, gold, warmth, applause.",

    # --- MARS (Action/Conflict) ---
    "MARS_ACTION_STYLE": "Direct, overwhelming, monarchical.",
    "MARS_CONFLICT_TRIGGER": "Disrespect to his authority or harm to his protected ones.",
    "MARS_SEXUAL_DRIVE_MODE": "Vital, generative, performative.",
    "CONFLICT_STANCE": "Dominate and protect.",

    # --- JUPITER (Growth - New!) ---
    "JUPITER_GROWTH_STRATEGY": "Expansion through benevolence and patronage.",
    "JUPITER_EXPANSION_FIELD": "Where he can be the 'Good King' to many.",
    "MAIN_GOAL_TYPE": "To build a legacy that outlasts the sun.",

    # --- SATURN (Limitation - New!) ---
    "SATURN_DISCIPLINE_MODE": "Rigid adherence to code and ceremony.",
    "SATURN_LIMITATION_STYLE": "Fear of weakness/ordinariness restricts his vulnerability.",
    "SATURN_LONG_TERM_ARC": "To ensure the dynasty survives his death.",

    # --- URANUS (Disruption - New!) ---
    "URANUS_REBELLION_STYLE": "Rebels against dull tradition by being shockingly bold.",
    "URANUS_GENIUS_LOCUS": "Sudden flashes of strategic brilliance in war.",

    # --- NEPTUNE (Dreams - New!) ---
    "NEPTUNE_DREAM_WORLD": "A utopia where everyone loves the King and no one suffers.",
    "NEPTUNE_ESCAPISM_STYLE": "Retreating into luxury and sycophancy.",

    # --- PLUTO (Power/Shadow - New!) ---
    "PLUTO_POWER_ARCHETYPE": "The Absolute Monarch.",
    "PLUTO_SHADOW_PATTERN": "Tyranny born from the terror of irrelevance.",
    "PLUTO_TRANSFORMATION_FIELD": "The loss of his crown or ego.",

    # --- NODES (Destiny - New!) ---
    "NN_LIFE_PATH_AXIS": "To move from self-aggrandizement to true service.",
    "SN_KARMIC_MEMORY": "A past of being a pampered prince who never suffered.",
    "CHIRON_CORE_WOUND": "The secret fear that he is unlovable without his crown.",

    # --- PHENOTYPE ---
    "PHENO_SKIN": "Deep Bronze, radiating a subtle dry heat.",
    "PHENO_HAIR": "A heavy, lion-like mane of coarse gold and rust strands.",
    "PHENO_EYES": "Amber-gold, unblinking and authoritative.",
    "PHENO_BUILD": "Broad-shouldered, barrel-chested, imposing verticality."
}

# 3. HERITAGE FLAGS
heritage_flags = ["RACE_FIRE", "CULT_LEO"]

def create_king():
    try:
        conn = pg8000.native.Connection(**DB_CONFIG)
        print("✅ Connected to database!")

        # 1. Update/Create Character
        exist_check = conn.run("SELECT char_id FROM characters WHERE name = :n", n=king_data['name'])
        
        if exist_check:
            char_id = exist_check[0][0]
            print(f"--> Updating: {king_data['name']}")
            conn.run("""
                UPDATE characters 
                SET age=:age, sex=:sex, race=:race, ethnicity=:eth, level=:lvl
                WHERE char_id=:cid
            """, cid=char_id, age=king_data['age'], sex=king_data['sex'], race=king_data['race'], eth=king_data['ethnicity'], lvl=king_data['level'])
            conn.run("DELETE FROM atomic_values WHERE char_id = :cid", cid=char_id)
        else:
            print(f"--> Creating: {king_data['name']}")
            result = conn.run("""
                INSERT INTO characters (name, archetype, level, age, sex, race, ethnicity, description)
                VALUES (:name, :arch, :lvl, :age, :sex, :race, :eth, :desc)
                RETURNING char_id;
            """, **king_data)
            char_id = result[0][0]

        # 2. Insert Data
        var_map = {row[0]: row[1] for row in conn.run("SELECT var_code, atomic_var_id FROM atomic_variable_def")}

        # Text Values
        for code, text in text_values.items():
            var_id = var_map.get(code)
            if var_id:
                conn.run("INSERT INTO atomic_values (char_id, atomic_var_id, value_text) VALUES (:cid, :vid, :val)", cid=char_id, vid=var_id, val=text)
            else:
                print(f"   ⚠️ Warning: Var Code '{code}' not found in DB!")

        # Flags
        for code in heritage_flags:
            var_id = var_map.get(code)
            if var_id:
                conn.run("INSERT INTO atomic_values (char_id, atomic_var_id, value_text) VALUES (:cid, :vid, 'Dominant Trait')", cid=char_id, vid=var_id)

        conn.close()
        
        # 3. AUTO-TRIGGER LOGIC
        astro_logic.refresh_all_logic()
        
        print(f"🎉 DONE! The Solar King now has a Full Chart.")

    except Exception as e:
        print("\n❌ ERROR:", e)

if __name__ == "__main__":
    create_king()