import pg8000.native
import json

# 1. DATABASE CONNECTION
DB_CONFIG = {
    "database": "atomic_astro_db",  
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1",  # <--- UPDATE THIS!
    "host": "localhost",
    "port": 5433
}

# 2. THE DATA (Overlay Models)
# This defines the "Books" (Models) and "Chapters" (Dimensions)
overlays_data = [
    {
        "code": "BIG_FIVE",
        "name": "Big Five (OCEAN)",
        "type": "scale_0_100",
        "desc": "The standard psychological model of personality traits.",
        "dimensions": [
            {"code": "OPENNESS", "name": "Openness", "min": 0, "max": 100},
            {"code": "CONSCIENTIOUSNESS", "name": "Conscientiousness", "min": 0, "max": 100},
            {"code": "EXTRAVERSION", "name": "Extraversion", "min": 0, "max": 100},
            {"code": "AGREEABLENESS", "name": "Agreeableness", "min": 0, "max": 100},
            {"code": "NEUROTICISM", "name": "Neuroticism", "min": 0, "max": 100}
        ]
    },
    {
        "code": "ENNEAGRAM",
        "name": "Enneagram",
        "type": "typology",
        "desc": "A model of human psyche principally understood and taught as a typology of nine interconnected personality types.",
        "dimensions": [
            {
                "code": "CORE_TYPE", 
                "name": "Core Type", 
                "options": ["Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Type 7", "Type 8", "Type 9"]
            },
            {
                "code": "WING", 
                "name": "Wing", 
                "options": ["1w9", "1w2", "2w1", "2w3", "3w2", "3w4", "4w3", "4w5", "5w4", "5w6", "6w5", "6w7", "7w6", "7w8", "8w7", "8w9", "9w8", "9w1"]
            }
        ]
    },
    {
        "code": "ATTACHMENT",
        "name": "Attachment Style",
        "type": "typology",
        "desc": "Psychological model describing the dynamics of long-term interpersonal relationships.",
        "dimensions": [
            {
                "code": "STYLE", 
                "name": "Primary Style", 
                "options": ["Secure", "Anxious-Preoccupied", "Dismissive-Avoidant", "Fearful-Avoidant"]
            }
        ]
    }
]

def seed_overlays():
    try:
        conn = pg8000.native.Connection(**DB_CONFIG)
        print("✅ Connected to database!")

        for model in overlays_data:
            print(f"--> Processing Model: {model['name']}")
            
            # 1. Insert the Model (The "Book")
            result = conn.run("""
                INSERT INTO overlay_model (model_code, name, model_type, description)
                VALUES (:code, :name, :type, :desc)
                ON CONFLICT (model_code) DO NOTHING
                RETURNING model_id;
            """, code=model['code'], name=model['name'], type=model['type'], desc=model['desc'])
            
            # Get the ID (newly created or looked up)
            if len(result) > 0:
                model_id = result[0][0]
            else:
                lookup = conn.run("SELECT model_id FROM overlay_model WHERE model_code = :code", code=model['code'])
                model_id = lookup[0][0]

            # 2. Insert the Dimensions (The "Chapters")
            for dim in model['dimensions']:
                # Handle JSON options (if they exist)
                options_json = json.dumps(dim.get('options')) if dim.get('options') else None
                
                conn.run("""
                    INSERT INTO overlay_model_dimension 
                    (model_id, dimension_code, name, min_value, max_value, enum_options)
                    VALUES (:mid, :code, :name, :minv, :maxv, :opts)
                    ON CONFLICT (model_id, dimension_code) DO NOTHING;
                """, 
                mid=model_id, 
                code=dim['code'], 
                name=dim['name'], 
                minv=dim.get('min'), 
                maxv=dim.get('max'), 
                opts=options_json
                )
                print(f"   -> Added Dimension: {dim['name']}")

        conn.close()
        print("\n🎉 SUCCESS! Overlay models seeded.")

    except Exception as e:
        print("\n❌ ERROR:", e)

if __name__ == "__main__":
    seed_overlays()