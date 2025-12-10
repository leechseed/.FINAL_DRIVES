import pg8000.native

DB_CONFIG = {
    "database": "atomic_astro_db",  
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1", 
    "host": "localhost",
    "port": 5433
}

# THE MASTER WIRING PLAN
# Connecting Lore (Planets) -> Mechanics (BFAS)
wiring_plan = [
    # --- EXTRAVERSION: ASSERTIVENESS (Dominance, Agency) ---
    {"source": "SUN_MOTIVATION_VECTOR", "target": "ASSERTIVENESS", "weight": 0.8},
    {"source": "SOCIAL_POWER_LEVEL",    "target": "ASSERTIVENESS", "weight": 1.0},
    {"source": "MARS_ACTION_STYLE",     "target": "ASSERTIVENESS", "weight": 1.2}, # Mars is the engine of agency
    {"source": "PLUTO_POWER_ARCHETYPE", "target": "ASSERTIVENESS", "weight": 0.5},

    # --- EXTRAVERSION: ENTHUSIASM (Sociability, Joy) ---
    {"source": "SUN_EGO_STYLE",           "target": "ENTHUSIASM", "weight": 1.0},
    {"source": "ASC_INTERACTION_STYLE",   "target": "ENTHUSIASM", "weight": 0.8},
    {"source": "VENUS_PLEASURE_METRICS",  "target": "ENTHUSIASM", "weight": 0.6}, # Venus likes fun

    # --- NEUROTICISM: VOLATILITY (Anger, Impulse) ---
    {"source": "MARS_CONFLICT_TRIGGER", "target": "VOLATILITY", "weight": 1.2},
    {"source": "MOON_TRIGGER_SET",      "target": "VOLATILITY", "weight": 0.8},
    {"source": "URANUS_REBELLION_STYLE","target": "VOLATILITY", "weight": 0.5},

    # --- NEUROTICISM: WITHDRAWAL (Anxiety, Depression) ---
    {"source": "MOON_NEED_CORE",        "target": "WITHDRAWAL", "weight": 1.0},
    {"source": "MOON_SURVIVAL_SCRIPT",  "target": "WITHDRAWAL", "weight": 1.0},
    {"source": "SATURN_LIMITATION_STYLE","target": "WITHDRAWAL", "weight": 0.8}, # Saturn restricts/depresses
    {"source": "NEPTUNE_ESCAPISM_STYLE","target": "WITHDRAWAL", "weight": 0.5},

    # --- AGREEABLENESS: COMPASSION (Empathy) ---
    {"source": "MOON_ATTACHMENT_PATTERN", "target": "COMPASSION", "weight": 1.0},
    {"source": "VENUS_LOVE_STYLE",        "target": "COMPASSION", "weight": 1.0},
    {"source": "NEPTUNE_DREAM_WORLD",     "target": "COMPASSION", "weight": 0.4}, # Neptune dissolves boundaries

    # --- AGREEABLENESS: POLITENESS (Manners, Norms) ---
    {"source": "ASC_INTERACTION_STYLE",   "target": "POLITENESS", "weight": 0.8},
    {"source": "VENUS_RELATIONAL_VALUES", "target": "POLITENESS", "weight": 1.0},
    {"source": "SATURN_DISCIPLINE_MODE",  "target": "POLITENESS", "weight": 0.5}, # Saturn likes rules

    # --- CONSCIENTIOUSNESS: INDUSTRIOUSNESS (Drive, Grit) ---
    {"source": "SUN_PRIDE_CENTER",        "target": "INDUSTRIOUSNESS", "weight": 0.8},
    {"source": "SATURN_DISCIPLINE_MODE",  "target": "INDUSTRIOUSNESS", "weight": 1.5}, # Saturn IS industry
    {"source": "MARS_ACTION_STYLE",       "target": "INDUSTRIOUSNESS", "weight": 0.5},

    # --- CONSCIENTIOUSNESS: ORDERLINESS (Structure, Cleanliness) ---
    {"source": "SATURN_LIMITATION_STYLE", "target": "ORDERLINESS", "weight": 0.5},
    {"source": "MERCURY_DECISION_PROCESS","target": "ORDERLINESS", "weight": 0.7}, # Logic requires order

    # --- OPENNESS: INTELLECT (Logic, Ideas) ---
    {"source": "MERCURY_COGNITION_STYLE", "target": "INTELLECT", "weight": 1.5}, # Mercury IS intellect
    {"source": "SUN_THEMATIC_QUESTION",   "target": "INTELLECT", "weight": 0.5},
    {"source": "URANUS_GENIUS_LOCUS",     "target": "INTELLECT", "weight": 0.8},

    # --- OPENNESS: CREATIVITY (Aesthetics, Fantasy) ---
    {"source": "VENUS_ATTRACTION_PROFILE","target": "OPENNESS_CREATIVE", "weight": 0.8},
    {"source": "NEPTUNE_DREAM_WORLD",     "target": "OPENNESS_CREATIVE", "weight": 1.2}, # Neptune IS fantasy
    {"source": "ASC_SURFACE_IMAGE",       "target": "OPENNESS_CREATIVE", "weight": 0.5}
]

def wire_bfas():
    try:
        conn = pg8000.native.Connection(**DB_CONFIG)
        print("✅ Connected. Wiring Full Solar System to BFAS...")

        # 1. Index IDs
        var_map = {}
        for row in conn.run("SELECT var_code, atomic_var_id FROM atomic_variable_def"):
            var_map[row[0]] = row[1]
            
        dim_map = {}
        for row in conn.run("SELECT dimension_code, dimension_id FROM overlay_model_dimension"):
            dim_map[row[0]] = row[1]

        # 2. Insert Wires
        count = 0
        skipped = 0
        for wire in wiring_plan:
            src_id = var_map.get(wire['source'])
            tgt_id = dim_map.get(wire['target'])
            
            if src_id and tgt_id:
                conn.run("""
                    INSERT INTO variable_mappings (atomic_var_id, dimension_id, weight)
                    VALUES (:vid, :did, :w)
                    ON CONFLICT (atomic_var_id, dimension_id) DO UPDATE 
                    SET weight = :w;
                """, vid=src_id, did=tgt_id, w=wire['weight'])
                count += 1
                print(f"   🔗 Wired: {wire['source']} -> {wire['target']}")
            else:
                skipped += 1
                missing = wire['source'] if not src_id else wire['target']
                # Only print warning if you want to debug missing vars
                # print(f"   ⚠️ Skipping: {missing} not found.")

        conn.close()
        print(f"\n🎉 SUCCESS! Established {count} logic connections.")
        if skipped > 0:
            print(f"   (Skipped {skipped} connections because those variables aren't seeded yet)")

    except Exception as e:
        print("\n❌ ERROR:", e)

if __name__ == "__main__":
    wire_bfas()