import pg8000.native

DB_CONFIG = {
    "database": "atomic_astro_db",  
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1",  
    "host": "localhost",
    "port": 5433
}

# The Missing Planets & Nodes
variables_data = [
    # --- MERCURY (Mind) ---
    {"sub": "MERCURY", "code": "MERCURY_COGNITION_STYLE", "name": "Cognition Style", "desc": "How they process information (Intuitive vs Logic)."},
    {"sub": "MERCURY", "code": "MERCURY_DECISION_PROCESS", "name": "Decision Process", "desc": "Fast/Impulsive vs Slow/Deliberate."},
    {"sub": "MERCURY", "code": "MERCURY_COMMUNICATION_STYLE", "name": "Communication Style", "desc": "How they speak and convey ideas."},
    {"sub": "MERCURY", "code": "MERCURY_SOCIAL_INTELLIGENCE_PROFILE", "name": "Social Intelligence", "desc": "Ability to read rooms and navigate politics."},

    # --- VENUS (Love/Values) ---
    {"sub": "VENUS", "code": "VENUS_LOVE_STYLE", "name": "Love Style", "desc": "How they express affection and romance."},
    {"sub": "VENUS", "code": "VENUS_ATTRACTION_PROFILE", "name": "Attraction Profile", "desc": "What they are magnetically drawn to."},
    {"sub": "VENUS", "code": "VENUS_RELATIONAL_VALUES", "name": "Relational Values", "desc": "What they value most in others (Loyalty, Status, Fun)."},
    {"sub": "VENUS", "code": "VENUS_PLEASURE_METRICS", "name": "Pleasure Metrics", "desc": "What brings them sensory joy and comfort."},

    # --- MARS (Action/Drive) ---
    {"sub": "MARS", "code": "MARS_ACTION_STYLE", "name": "Action Style", "desc": "How they pursue goals (Direct, Strategic, Chaotic)."},
    {"sub": "MARS", "code": "MARS_CONFLICT_TRIGGER", "name": "Conflict Trigger", "desc": "What makes them fight."},
    {"sub": "MARS", "code": "MARS_SEXUAL_DRIVE_MODE", "name": "Sexual/Vital Drive", "desc": "The nature of their libido and life-force energy."},
    {"sub": "MARS", "code": "CONFLICT_STANCE", "name": "Conflict Stance", "desc": "Fight, Flight, Freeze, or Negotiate."},

    # --- JUPITER (Growth) ---
    {"sub": "JUPITER", "code": "JUPITER_GROWTH_STRATEGY", "name": "Growth Strategy", "desc": "How they expand their influence and knowledge."},
    {"sub": "JUPITER", "code": "JUPITER_EXPANSION_FIELD", "name": "Expansion Field", "desc": "Where they feel luckiest and most abundant."},
    {"sub": "JUPITER", "code": "MAIN_GOAL_TYPE", "name": "Main Quest Goal", "desc": "The ultimate prize they are chasing."},

    # --- SATURN (Structure) ---
    {"sub": "SATURN", "code": "SATURN_DISCIPLINE_MODE", "name": "Discipline Mode", "desc": "How they handle responsibility and hard work."},
    {"sub": "SATURN", "code": "SATURN_LIMITATION_STYLE", "name": "Limitation Style", "desc": "Where they feel restricted, blocked, or inadequate."},
    {"sub": "SATURN", "code": "SATURN_LONG_TERM_ARC", "name": "Long Term Ambition", "desc": "The mountain they are slowly climbing."},

    # --- URANUS (Change) ---
    {"sub": "URANUS", "code": "URANUS_REBELLION_STYLE", "name": "Rebellion Style", "desc": "How they break rules and disrupt the status quo."},
    {"sub": "URANUS", "code": "URANUS_GENIUS_LOCUS", "name": "Locus of Genius", "desc": "Where they are brilliant and unpredictable."},

    # --- NEPTUNE (Dreams) ---
    {"sub": "NEPTUNE", "code": "NEPTUNE_DREAM_WORLD", "name": "Dream World", "desc": "The fantasy they prefer over reality."},
    {"sub": "NEPTUNE", "code": "NEPTUNE_ESCAPISM_STYLE", "name": "Escapism Style", "desc": "How they check out when life gets too hard."},

    # --- PLUTO (Power) ---
    {"sub": "PLUTO", "code": "PLUTO_POWER_ARCHETYPE", "name": "Power Archetype", "desc": "How they wield control and dominance."},
    {"sub": "PLUTO", "code": "PLUTO_SHADOW_PATTERN", "name": "Shadow Pattern", "desc": "The dark traits they project onto others."},
    {"sub": "PLUTO", "code": "PLUTO_TRANSFORMATION_FIELD", "name": "Transformation Field", "desc": "Where they must die and be reborn."},

    # --- NODES & CHIRON ---
    {"sub": "NORTH_NODE", "code": "NN_LIFE_PATH_AXIS", "name": "Destiny Axis", "desc": "The direction their soul wants to go."},
    {"sub": "SOUTH_NODE", "code": "SN_KARMIC_MEMORY", "name": "Karmic Memory", "desc": "The comfort zone they are stuck in."},
    {"sub": "CHIRON", "code": "CHIRON_CORE_WOUND", "name": "Core Wound", "desc": "The unhealable hurt they carry."},
]

def seed_planets():
    try:
        conn = pg8000.native.Connection(**DB_CONFIG)
        print("✅ Connected. Fetching Subsystem IDs...")

        # 1. Fetch Subsystem IDs
        subsystem_map = {}
        rows = conn.run("SELECT subsystem_code, subsystem_id FROM subsystems")
        for row in rows:
            subsystem_map[row[0]] = row[1]

        # 2. Insert Variables
        count = 0
        for var in variables_data:
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
        print(f"\n🎉 SUCCESS! Inserted {count} planetary variables.")

    except Exception as e:
        print("\n❌ ERROR:", e)

if __name__ == "__main__":
    seed_planets()