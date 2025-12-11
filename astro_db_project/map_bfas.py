import pg8000.native

DB_CONFIG = {
    "database": "atomic_astro_db",  
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1", 
    "host": "localhost",
    "port": 5433
}

# --- THE 1-12 IMPACT SCALE ---
TRACE = 1       # Barely noticeable
NUANCE = 3      # Flavor / Tilt
STANDARD = 5    # Baseline behavior (The old "1.0")
STRONG = 8      # Strong Drive (The old "1.5")
COMPULSIVE = 10 # Overwhelming urge
ABSOLUTE = 12   # Unbreakable law

def add_mapping(conn, source, trait, weight):
    # We explicitly cast weight to INT to ensure no decimals sneak in
    weight = int(weight)
    conn.run("""
        INSERT INTO bfas_mapping (source_value, target_trait, weight, source_type)
        VALUES (:src, :trait, :w, 'ASTRO')
        ON CONFLICT (source_value, target_trait) 
        DO UPDATE SET weight = :w
    """, src=source, trait=trait, w=weight)

def wire_bfas():
    try:
        conn = pg8000.native.Connection(**DB_CONFIG)
        
        # --- 1. SUN (Identity / Ego) ---
        # Impact: STRONG (8) because Ego is a major driver
        add_mapping(conn, "SUN_MOTIVATION_VECTOR", "Assertiveness", STRONG)
        add_mapping(conn, "SUN_EGO_STYLE", "Enthusiasm", STRONG) 
        add_mapping(conn, "SUN_PRIDE_CENTER", "Industriousness", STRONG)
        add_mapping(conn, "SUN_THEMATIC_QUESTION", "Intellect", STANDARD) # More philosophical

        # --- 2. MOON (Emotional Core) ---
        # Impact: COMPULSIVE (10) because Trauma/Safety overrides logic
        add_mapping(conn, "MOON_NEED_CORE", "Withdrawal", COMPULSIVE)
        add_mapping(conn, "MOON_SURVIVAL_SCRIPT", "Withdrawal", COMPULSIVE)
        add_mapping(conn, "MOON_TRIGGER_SET", "Volatility", COMPULSIVE)
        add_mapping(conn, "MOON_ATTACHMENT_PATTERN", "Compassion", STRONG)

        # --- 3. MERCURY (Mind) ---
        # Impact: STANDARD (5) to STRONG (8)
        add_mapping(conn, "MERCURY_COGNITION_STYLE", "Intellect", STRONG)
        add_mapping(conn, "MERCURY_DECISION_PROCESS", "Orderliness", STANDARD)
        # Note: Communication style is narrative, affects Politeness/Enthusiasm
        add_mapping(conn, "MERCURY_COMMUNICATION_STYLE", "Enthusiasm", STANDARD)

        # --- 4. VENUS (Desire) ---
        # Impact: STRONG (8)
        add_mapping(conn, "VENUS_LOVE_STYLE", "Compassion", STRONG)
        add_mapping(conn, "VENUS_PLEASURE_METRICS", "Enthusiasm", STRONG)
        add_mapping(conn, "VENUS_RELATIONAL_VALUES", "Politeness", STANDARD)
        add_mapping(conn, "VENUS_ATTRACTION_PROFILE", "Openness", STANDARD)

        # --- 5. MARS (Conflict) ---
        # Impact: COMPULSIVE (10) for Violence/Action
        add_mapping(conn, "MARS_ACTION_STYLE", "Assertiveness", COMPULSIVE)
        add_mapping(conn, "MARS_ACTION_STYLE", "Industriousness", STANDARD) # Takes effort to fight
        add_mapping(conn, "MARS_CONFLICT_TRIGGER", "Volatility", COMPULSIVE)
        add_mapping(conn, "MARS_SEXUAL_DRIVE_MODE", "Enthusiasm", STANDARD)

        # --- 6. JUPITER (Growth) ---
        # Impact: STANDARD (5)
        add_mapping(conn, "JUPITER_GROWTH_STRATEGY", "Openness", STRONG)
        add_mapping(conn, "JUPITER_EXPANSION_FIELD", "Assertiveness", STANDARD)
        add_mapping(conn, "MAIN_GOAL_TYPE", "Industriousness", STANDARD)

        # --- 7. SATURN (Limitation) ---
        # Impact: COMPULSIVE (10) for Fear/Restriction
        add_mapping(conn, "SATURN_LIMITATION_STYLE", "Withdrawal", COMPULSIVE) # Fear
        add_mapping(conn, "SATURN_LIMITATION_STYLE", "Orderliness", STRONG)    # Control
        add_mapping(conn, "SATURN_DISCIPLINE_MODE", "Industriousness", STRONG)
        add_mapping(conn, "SATURN_DISCIPLINE_MODE", "Politeness", STANDARD)     # Social Protocol

        # --- 8. URANUS (Chaos) ---
        # Impact: STRONG (8)
        add_mapping(conn, "URANUS_REBELLION_STYLE", "Volatility", STRONG)
        add_mapping(conn, "URANUS_REBELLION_STYLE", "Openness", STRONG)       # Radical Ideas
        add_mapping(conn, "URANUS_GENIUS_LOCUS", "Intellect", STRONG)

        # --- 9. NEPTUNE (Illusion) ---
        # Impact: COMPULSIVE (10) for Addiction/Escape
        add_mapping(conn, "NEPTUNE_ESCAPISM_STYLE", "Withdrawal", COMPULSIVE)
        add_mapping(conn, "NEPTUNE_DREAM_WORLD", "Openness", COMPULSIVE)      # Fantasy
        add_mapping(conn, "NEPTUNE_DREAM_WORLD", "Compassion", STANDARD)      # Merging

        # --- 10. PLUTO (Power) ---
        # Impact: ABSOLUTE (12) - The Shadow Logic
        add_mapping(conn, "PLUTO_POWER_ARCHETYPE", "Assertiveness", ABSOLUTE)
        add_mapping(conn, "PLUTO_SHADOW_PATTERN", "Volatility", STRONG)       # Manipulation
        add_mapping(conn, "PLUTO_TRANSFORMATION_FIELD", "Openness", STRONG)   # Forced Change

        conn.close()
        print("✅ BFAS Wiring Complete (Integer Scale 1-12).")

    except Exception as e:
        print(f"❌ ERROR in map_bfas: {e}")

if __name__ == "__main__":
    wire_bfas()