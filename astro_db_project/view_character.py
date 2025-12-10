import pg8000.native

DB_CONFIG = {
    "database": "atomic_astro_db",  
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1", 
    "host": "localhost",
    "port": 5433
}

def print_header(text):
    print(f"\n{'='*60}")
    print(f" {text.upper()}")
    print(f"{'='*60}")

def view_character(char_name):
    try:
        conn = pg8000.native.Connection(**DB_CONFIG)
        
        # 1. FETCH BASIC INFO + DEMOGRAPHICS
        res = conn.run("""
            SELECT name, age, sex, race, ethnicity, archetype, level, description 
            FROM characters WHERE name = :n
        """, n=char_name)
        
        if not res:
            print(f"\n❌ Character '{char_name}' not found!")
            conn.close()
            return

        c = res[0]
        # Basic Header
        print("\n\n")
        print(f"╔{'═'*58}╗")
        print(f"║ {c[0]:<56} ║") # Name
        print(f"╠{'═'*58}╣")
        print(f"║ Arch: {c[5]:<50} ║")
        print(f"║ Lvl: {c[6]:<2} | Age: {c[1]:<3} | Sex: {c[2]:<10}                      ║")
        print(f"╠{'═'*58}╣")
        # Heritage Display
        print(f"║ BIO:  {c[3]:<50} ║")
        print(f"║ CULT: {c[4]:<50} ║")
        print(f"╚{'═'*58}╝")
        print(f"📜 \"{c[7]}\"")

        # 2. FETCH PHENOTYPE (Visuals)
        # We look for variables starting with PHENO_
        pheno_rows = conn.run("""
            SELECT v.name, val.value_text 
            FROM atomic_values val
            JOIN atomic_variable_def v ON val.atomic_var_id = v.atomic_var_id
            WHERE val.char_id = (SELECT char_id FROM characters WHERE name = :n)
            AND v.var_code LIKE 'PHENO_%'
            ORDER BY v.subsystem_id
        """, n=char_name)

        if pheno_rows:
            print_header("Phenotype (Appearance)")
            for r in pheno_rows:
                print(f"• {r[0]}: {r[1]}")

        # 3. FETCH LORE (The Atomic Text)
        print_header("The Lore (Atomic Variables)")
        # We exclude AGE_ and PHENO_ and RACE_ triggers to keep this clean
        lore_rows = conn.run("""
            SELECT v.name, val.value_text 
            FROM atomic_values val
            JOIN atomic_variable_def v ON val.atomic_var_id = v.atomic_var_id
            WHERE val.char_id = (SELECT char_id FROM characters WHERE name = :n)
            AND v.var_code NOT LIKE 'AGE_%' 
            AND v.var_code NOT LIKE 'PHENO_%'
            AND val.value_text != 'Dominant Trait' -- Hide technical flags
            ORDER BY v.subsystem_id
        """, n=char_name)
        
        for r in lore_rows:
            print(f"• {r[0]}:")
            print(f"  └─ \"{r[1]}\"")

        # 4. FETCH MECHANICS (The Calculated Stats)
        print_header("The Engine (Calculated BFAS Stats)")
        stats = conn.run("""
            SELECT 
                od.name AS trait,
                SUM(vm.weight) AS total_score,
                string_agg(v.name, ', ') as sources
            FROM characters c
            JOIN atomic_values val ON c.char_id = val.char_id
            JOIN variable_mappings vm ON val.atomic_var_id = vm.atomic_var_id
            JOIN atomic_variable_def v ON val.atomic_var_id = v.atomic_var_id
            JOIN overlay_model_dimension od ON vm.dimension_id = od.dimension_id
            WHERE c.name = :n
            GROUP BY od.name
            ORDER BY total_score DESC
        """, n=char_name)

        print(f"{'TRAIT':<25} | {'SCORE':<5} | {'SOURCES'}")
        print("-" * 80)
        for s in stats:
            score = float(s[1])
            bar_len = int(score * 3)
            bar = "█" * bar_len 
            # Show negative bars differently if needed, but for now simple positive visualization
            if score < 0:
                bar = "░" * abs(bar_len)
            
            print(f"{s[0]:<25} | {score:>5.1f} | {s[2]}")

        conn.close()

    except Exception as e:
        print("\n❌ ERROR:", e)

if __name__ == "__main__":
    # THIS IS THE UPDATE: It asks for input now!
    print("\n🔮 ATOMIC ASTROLOGY VIEWER")
    target = input("Enter Character Name (Press Enter for 'The Solar King'): ").strip()
    
    if not target:
        target = "The Solar King"
        
    view_character(target)