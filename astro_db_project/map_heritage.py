import pg8000.native

DB_CONFIG = {
    "database": "atomic_astro_db",  
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1", 
    "host": "localhost",
    "port": 5433
}

# THE HERITAGE WIRING PLAN
# Connecting 4 Races + 12 Cultures -> BFAS Mechanics
wiring_plan = [
    # --- BIOLOGICAL RACES (ELEMENTS) ---
    # Fire-Kin (Combustion)
    {"source": "RACE_FIRE", "target": "ASSERTIVENESS", "weight": 1.5},
    {"source": "RACE_FIRE", "target": "VOLATILITY", "weight": 1.0},
    {"source": "RACE_FIRE", "target": "WITHDRAWAL", "weight": -1.0}, # Hard to repress fire
    
    # Earth-Kin (Stability)
    {"source": "RACE_EARTH", "target": "ORDERLINESS", "weight": 1.5},
    {"source": "RACE_EARTH", "target": "INDUSTRIOUSNESS", "weight": 1.0},
    {"source": "RACE_EARTH", "target": "VOLATILITY", "weight": -1.0}, # Slow to anger
    
    # Air-Kin (Circulation)
    {"source": "RACE_AIR", "target": "ENTHUSIASM", "weight": 1.5},
    {"source": "RACE_AIR", "target": "INTELLECT", "weight": 1.0},
    {"source": "RACE_AIR", "target": "ORDERLINESS", "weight": -0.5}, # Scattered
    
    # Water-Kin (Immersion)
    {"source": "RACE_WATER", "target": "COMPASSION", "weight": 1.5},
    {"source": "RACE_WATER", "target": "OPENNESS_CREATIVE", "weight": 1.0},
    {"source": "RACE_WATER", "target": "WITHDRAWAL", "weight": 0.5}, # Can be moody

    # --- ZODIAC CULTURES ---
    # Aries: The Vanguard (Strength/Honor)
    {"source": "CULT_ARIES", "target": "ASSERTIVENESS", "weight": 1.5},
    {"source": "CULT_ARIES", "target": "POLITENESS", "weight": -0.5}, # Blunt
    
    # Taurus: The Builders (Cultivation/Comfort)
    {"source": "CULT_TAURUS", "target": "INDUSTRIOUSNESS", "weight": 1.2},
    {"source": "CULT_TAURUS", "target": "ENTHUSIASM", "weight": 0.5}, # Jovial
    
    # Gemini: The Weavers (Trade/Wit)
    {"source": "CULT_GEMINI", "target": "INTELLECT", "weight": 1.5},
    {"source": "CULT_GEMINI", "target": "ENTHUSIASM", "weight": 1.0},
    
    # Cancer: The Hearth (Clan/Memory)
    {"source": "CULT_CANCER", "target": "COMPASSION", "weight": 1.5},
    {"source": "CULT_CANCER", "target": "WITHDRAWAL", "weight": 0.8}, # Protective shell
    
    # Leo: The Regents (Performance/Pride)
    {"source": "CULT_LEO", "target": "ENTHUSIASM", "weight": 1.5},    # Social dominance
    {"source": "CULT_LEO", "target": "ASSERTIVENESS", "weight": 1.0},
    
    # Virgo: The Architects (Service/Precision)
    {"source": "CULT_VIRGO", "target": "ORDERLINESS", "weight": 1.5},
    {"source": "CULT_VIRGO", "target": "INDUSTRIOUSNESS", "weight": 1.0},
    
    # Libra: The Diplomats (Harmony/Aesthetic)
    {"source": "CULT_LIBRA", "target": "POLITENESS", "weight": 2.0},
    {"source": "CULT_LIBRA", "target": "OPENNESS_CREATIVE", "weight": 0.8},
    
    # Scorpio: The Deep (Secrets/Power)
    {"source": "CULT_SCORPIO", "target": "WITHDRAWAL", "weight": 1.0}, # Private
    {"source": "CULT_SCORPIO", "target": "INTELLECT", "weight": 1.0},  # Investigative
    
    # Sagittarius: The Voyagers (Truth/Freedom)
    {"source": "CULT_SAGITTARIUS", "target": "OPENNESS_CREATIVE", "weight": 1.5},
    {"source": "CULT_SAGITTARIUS", "target": "ENTHUSIASM", "weight": 1.0},
    
    # Capricorn: The Elders (Duty/History)
    {"source": "CULT_CAPRICORN", "target": "INDUSTRIOUSNESS", "weight": 1.5},
    {"source": "CULT_CAPRICORN", "target": "POLITENESS", "weight": 1.0}, # Formal
    
    # Aquarius: The Exiles (Ideas/Future)
    {"source": "CULT_AQUARIUS", "target": "INTELLECT", "weight": 1.5},
    {"source": "CULT_AQUARIUS", "target": "OPENNESS_CREATIVE", "weight": 1.0}, # Radical ideas
    
    # Pisces: The Mystics (Belief/Unity)
    {"source": "CULT_PISCES", "target": "OPENNESS_CREATIVE", "weight": 2.0},
    {"source": "CULT_PISCES", "target": "COMPASSION", "weight": 1.0}
]

def wire_heritage():
    try:
        conn = pg8000.native.Connection(**DB_CONFIG)
        print("✅ Connected. Wiring Heritage System...")

        var_map = {row[0]: row[1] for row in conn.run("SELECT var_code, atomic_var_id FROM atomic_variable_def")}
        dim_map = {row[0]: row[1] for row in conn.run("SELECT dimension_code, dimension_id FROM overlay_model_dimension")}

        count = 0
        for wire in wiring_plan:
            src_id = var_map.get(wire['source'])
            tgt_id = dim_map.get(wire['target'])
            
            if src_id and tgt_id:
                conn.run("""
                    INSERT INTO variable_mappings (atomic_var_id, dimension_id, weight)
                    VALUES (:vid, :did, :w)
                    ON CONFLICT (atomic_var_id, dimension_id) DO UPDATE SET weight = :w;
                """, vid=src_id, did=tgt_id, w=wire['weight'])
                count += 1
                print(f"   🔗 Wired: {wire['source']} -> {wire['target']}")
            else:
                 print(f"   ⚠️ Skipping: {wire['source']}")

        conn.close()
        print(f"\n🎉 SUCCESS! Connected {count} Heritage traits to the engine.")

    except Exception as e:
        print("\n❌ ERROR:", e)

if __name__ == "__main__":
    wire_heritage()