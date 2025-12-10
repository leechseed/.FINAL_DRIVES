import pg8000.native

DB_CONFIG = {
    "database": "atomic_astro_db",  
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1",  # <--- UPDATE THIS!
    "host": "localhost",
    "port": 5433
}

# The BFAS Model: 10 Variables
bfas_data = {
    "code": "BFAS",
    "name": "Big Five Aspects Scale (DeYoung)",
    "type": "scale_0_100",
    "desc": "A 10-aspect refinement of the Big Five, separating distinct behavioral drivers.",
    "dimensions": [
        # NEUROTICISM
        {"code": "VOLATILITY", "name": "Volatility (Anger/Impulse)", "min": 0, "max": 100},
        {"code": "WITHDRAWAL", "name": "Withdrawal (Anxiety/Depression)", "min": 0, "max": 100},
        
        # AGREEABLENESS
        {"code": "COMPASSION", "name": "Compassion (Empathy)", "min": 0, "max": 100},
        {"code": "POLITENESS", "name": "Politeness (Social Norms)", "min": 0, "max": 100},
        
        # CONSCIENTIOUSNESS
        {"code": "INDUSTRIOUSNESS", "name": "Industriousness (Drive/Grit)", "min": 0, "max": 100},
        {"code": "ORDERLINESS", "name": "Orderliness (Structure/Clean)", "min": 0, "max": 100},
        
        # EXTRAVERSION
        {"code": "ENTHUSIASM", "name": "Enthusiasm (Sociability/Joy)", "min": 0, "max": 100},
        {"code": "ASSERTIVENESS", "name": "Assertiveness (Dominance/Agency)", "min": 0, "max": 100},
        
        # OPENNESS
        {"code": "INTELLECT", "name": "Intellect (Logic/Ideas)", "min": 0, "max": 100},
        {"code": "OPENNESS_CREATIVE", "name": "Openness (Art/Fantasy)", "min": 0, "max": 100}
    ]
}

def seed_bfas():
    try:
        conn = pg8000.native.Connection(**DB_CONFIG)
        print("✅ Connected. Seeding BFAS...")

        # 1. Insert the Model
        result = conn.run("""
            INSERT INTO overlay_model (model_code, name, model_type, description)
            VALUES (:code, :name, :type, :desc)
            ON CONFLICT (model_code) DO NOTHING
            RETURNING model_id;
        """, code=bfas_data['code'], name=bfas_data['name'], type=bfas_data['type'], desc=bfas_data['desc'])
        
        # Handle case where model already exists vs created new
        if len(result) > 0:
            model_id = result[0][0]
        else:
            lookup = conn.run("SELECT model_id FROM overlay_model WHERE model_code = :code", code=bfas_data['code'])
            model_id = lookup[0][0]

        # 2. Insert the 10 Dimensions
        for dim in bfas_data['dimensions']:
            conn.run("""
                INSERT INTO overlay_model_dimension (model_id, dimension_code, name, min_value, max_value)
                VALUES (:mid, :code, :name, :minv, :maxv)
                ON CONFLICT (model_id, dimension_code) DO NOTHING;
            """, mid=model_id, code=dim['code'], name=dim['name'], minv=dim['min'], maxv=dim['max'])
            print(f"   -> Added Aspect: {dim['name']}")

        conn.close()
        print("\n🎉 SUCCESS! BFAS Model seeded with 10 aspects.")

    except Exception as e:
        print("\n❌ ERROR:", e)

if __name__ == "__main__":
    seed_bfas()