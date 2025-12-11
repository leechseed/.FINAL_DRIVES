import pg8000.native

# --- IMPORT YOUR WIRING SCRIPTS ---
import map_bfas         # Core Astrology -> Psychology mappings
import map_heritage     # Race/Culture -> Psychology mappings
import map_age          # Age Spiral -> Psychology mappings

DB_CONFIG = {
    "database": "atomic_astro_db",  
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1", 
    "host": "localhost",
    "port": 5433
}

def calculate_bfas_scores(conn):
    """
    The Physics Engine.
    Calculates final personality scores based on:
    1. Base Weights (from map_bfas)
    2. Character Resonance (The Volume Knob 1-12)
    """
    print("   [5/5] Calculating BFAS Scores (with Resonance)...")

    # 1. Ensure Score Table Exists
    conn.run("""
        CREATE TABLE IF NOT EXISTS bfas_scores (
            score_id SERIAL PRIMARY KEY,
            char_id INT REFERENCES characters(char_id) ON DELETE CASCADE,
            trait_name VARCHAR(50),
            score FLOAT,
            UNIQUE(char_id, trait_name)
        );
    """)

    # 2. Get All Characters
    chars = conn.run("SELECT char_id, name FROM characters")

    for char in chars:
        cid, name = char
        
        # Clear old scores for this character to ensure a fresh calc
        conn.run("DELETE FROM bfas_scores WHERE char_id = :cid", cid=cid)

        # 3. Fetch Active Variables + Resonance Volume
        # This joins the character's values with their specific 'Volume' settings
        # If no volume is set, it defaults to 6 (Standard/100%)
        rows = conn.run("""
            SELECT 
                av.value_text, 
                def.var_code,
                sub.subsystem_code,
                COALESCE(res.volume, 6) as volume
            FROM atomic_values av
            JOIN atomic_variable_def def ON av.atomic_var_id = def.atomic_var_id
            JOIN subsystems sub ON def.subsystem_id = sub.subsystem_id
            LEFT JOIN character_resonance res ON (av.char_id = res.char_id AND sub.subsystem_code = res.subsystem_code)
            WHERE av.char_id = :cid
        """, cid=cid)

        scores = {}

        # 4. The Math Loop
        for row in rows:
            val_text, var_code, sub_code, volume = row
            
            # THE RESONANCE FORMULA
            # Volume 6 = 1.0x (Standard)
            # Volume 12 = 2.0x (Dominant)
            # Volume 1 = 0.16x (Trace)
            multiplier = volume / 6.0 

            # Find Mappings
            # We check if the TEXT implies a trait (e.g. 'CULT_CANCER' -> Withdrawal)
            # OR if the VARIABLE itself implies a trait (e.g. 'MOON_SURVIVAL_SCRIPT' -> Withdrawal)
            # Note: This relies on 'bfas_mapping' being populated by your map_*.py scripts
            mappings = conn.run("""
                SELECT target_trait, weight 
                FROM bfas_mapping 
                WHERE source_value = :val 
                   OR source_value = :code
            """, val=val_text, code=var_code)

            for m in mappings:
                trait = m[0]
                base_weight = float(m[1])
                
                # Apply the Volume Knob
                final_impact = base_weight * multiplier
                
                if trait not in scores: scores[trait] = 0.0
                scores[trait] += final_impact

        # 5. Save Final Scores
        for trait, score in scores.items():
            # Round to 1 decimal for clean display (e.g. 4.1)
            final_score = round(score, 1)
            conn.run("""
                INSERT INTO bfas_scores (char_id, trait_name, score) 
                VALUES (:cid, :t, :s)
            """, cid=cid, t=trait, s=final_score)

def refresh_all_logic():
    """
    The Master Switch.
    Runs every logic script you have installed.
    """
    try:
        conn = pg8000.native.Connection(**DB_CONFIG)
        print("\n⚙️  SYSTEM: Refreshing Logic Layer...")

        # 1. RUN THE WIRING SCRIPTS (The Cables)
        # These populate the 'bfas_mapping' table
        print("   [1/3] Wiring Astrology -> BFAS...")
        map_bfas.wire_bfas()
        
        print("   [2/3] Wiring Heritage -> BFAS...")
        map_heritage.wire_heritage()
        
        print("   [3/3] Wiring Age -> BFAS...")
        map_age.wire_age()

        # 2. RUN AGE ASSIGNMENTS (The Spiral)
        print("   [4/5] Calculating Age Spirals...")
        ranges = [
            (1, 12, "AGE_CHILDHOOD"), (12, 18, "AGE_ADOLESCENCE"),
            (18, 24, "AGE_PILGRIM"), (24, 30, "AGE_ADULTHOOD"),
            (30, 36, "AGE_CLASSIFICATION"), (36, 42, "AGE_REVISITATION"),
            (42, 48, "AGE_ASCENTION"), (48, 54, "AGE_MASTERY"),
            (54, 150, "AGE_ELDER")
        ]
        
        # Helper to get ID map
        var_map = {row[0]: row[1] for row in conn.run("SELECT var_code, atomic_var_id FROM atomic_variable_def")}
        
        # Clear old spiral assignments
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

        # 3. RUN THE PHYSICS ENGINE (Calculate Stats)
        calculate_bfas_scores(conn)

        conn.close()
        print("✅ SYSTEM: All Systems synced. The engine is hot.\n")

    except Exception as e:
        print(f"❌ SYSTEM ERROR: {e}")

if __name__ == "__main__":
    refresh_all_logic()