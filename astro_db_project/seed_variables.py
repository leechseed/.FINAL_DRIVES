import pg8000.native

# 1. DATABASE CONNECTION
DB_CONFIG = {
    "database": "atomic_astro_db",  
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1",  # <--- UPDATE THIS!
    "host": "localhost",
    "port": 5433
}

# 2. THE DATA (Core Identity Variables)
# This maps the specific variables to their Subsystem Code
variables_data = [
    # --- SUN (Identity) ---
    {"sub": "SUN", "code": "SUN_IDENTITY_AXIS", "name": "Identity Axis", "desc": "How the character fundamentally sees themselves."},
    {"sub": "SUN", "code": "SUN_MOTIVATION_VECTOR", "name": "Motivation Vector", "desc": "The main conscious drive that pulls them forward."},
    {"sub": "SUN", "code": "SUN_EGO_STYLE", "name": "Ego Style", "desc": "The way they show off, assert themselves, and protect their pride."},
    {"sub": "SUN", "code": "SUN_THEMATIC_QUESTION", "name": "Thematic Question", "desc": "The big personal question they keep bumping into."},
    {"sub": "SUN", "code": "SUN_PRIDE_CENTER", "name": "Pride Center", "desc": "The thing they are most proud of and sensitive about losing."},
    
    # --- MOON (Emotion) ---
    {"sub": "MOON", "code": "MOON_NEED_CORE", "name": "Core Emotional Need", "desc": "The emotional condition they must have to feel safe."},
    {"sub": "MOON", "code": "MOON_EMOTIONAL_STYLE", "name": "Emotional Style", "desc": "How they feel, express, and cool down emotionally."},
    {"sub": "MOON", "code": "MOON_TRIGGER_SET", "name": "Trigger Set", "desc": "Specific situations or behaviors that reliably upset them."},
    {"sub": "MOON", "code": "MOON_ATTACHMENT_PATTERN", "name": "Attachment Pattern", "desc": "The way they bond, cling, avoid, or sabotage relationships."},
    {"sub": "MOON", "code": "MOON_SURVIVAL_SCRIPT", "name": "Survival Script", "desc": "The automatic behavior they jump to under emotional threat."},

    # --- ASCENDANT (Persona) ---
    {"sub": "ASC", "code": "ASC_SURFACE_IMAGE", "name": "Surface Image", "desc": "The vibe they give off at a glance."},
    {"sub": "ASC", "code": "ASC_INTERACTION_STYLE", "name": "Interaction Style", "desc": "Their default way of engaging people in social situations."},
    {"sub": "ASC", "code": "ASC_MASK_VS_CORE_GAP", "name": "Mask vs Core Gap", "desc": "How different their outside persona is from their inner reality."},
    {"sub": "ASC", "code": "SOCIAL_POWER_LEVEL", "name": "Social Power Level", "desc": "How much weight their presence carries in a room."}
]

def seed_variables():
    try:
        conn = pg8000.native.Connection(**DB_CONFIG)
        print("✅ Connected. Fetching Subsystem IDs...")

        # 1. Fetch Subsystem IDs so we know where to put the variables
        # We create a dictionary like: {'SUN': 1, 'MOON': 2}
        subsystem_map = {}
        rows = conn.run("SELECT subsystem_code, subsystem_id FROM subsystems")
        for row in rows:
            subsystem_map[row[0]] = row[1]

        # 2. Insert Variables
        count = 0
        for var in variables_data:
            # Look up the ID for "SUN", "MOON", etc.
            sub_id = subsystem_map.get(var['sub'])
            
            if sub_id:
                conn.run("""
                    INSERT INTO atomic_variable_def (subsystem_id, var_code, name, description)
                    VALUES (:sid, :code, :name, :desc)
                    ON CONFLICT (var_code) DO NOTHING;
                """, sid=sub_id, code=var['code'], name=var['name'], desc=var['desc'])
                count += 1
                print(f"   -> Added {var['code']}")
            else:
                print(f"   ⚠️ WARNING: Subsystem '{var['sub']}' not found in DB!")

        conn.close()
        print(f"\n🎉 SUCCESS! Inserted {count} atomic variables.")

    except Exception as e:
        print("\n❌ ERROR:", e)

if __name__ == "__main__":
    seed_variables()