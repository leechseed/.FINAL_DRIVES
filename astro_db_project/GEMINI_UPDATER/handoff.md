# SYSTEM HANDOFF: ATOMIC ASTROLOGY (PHASE 2)

**PROJECT OVERVIEW**
I am building a narrative RPG character database using Python (Streamlit/PG8000) and PostgreSQL.
We are transitioning from a "Prototype" phase (using unstructured text dictionaries) to an "Architecture" phase (using relational tables).

**1. THE NARRATIVE TONE (DO NOT FORGET THIS)**
The writing style is "Neo-Mythic," blending grounded realism with high-concept existentialism.

- **Sun:** 80% _Life is Strange_ / 20% _Cyberpunk 2077_ (Identity/Ego).
- **Moon:** 100% _Neon Genesis Evangelion_ (Trauma/Defense/Isolation).
- **Mars:** _Fight Club_ + _The Social Network_ (Aggression/Sabotage).
- **Saturn:** 100% _GTA V_ (Institutional Debt/Cynicism).
- **Pluto:** _The Bible_ + _The Story of Us_ (Total Power/Erasure).
- _Note: See `archetype_text.py` for the full library._

**2. THE MATH ENGINE**

- **Logic:** Weighted Tag Summation.
- **Scale:** Integer 1-12 (Trace to Absolute).
- **Resonance:** A multiplier (Volume Knob) applied per planet per character.

**3. THE MISSION: "THE GREAT MIGRATION"**
We have decided to refactor the database schema to support "User Roles" (Architect, Author, Director).
We are abandoning the old `atomic_values` table structure.
We are moving to a relational structure with `char_placements` and `library_archetypes`.

**THE NEW SCHEMA (SCHEMA_V2.SQL)**
Please analyze this proposed schema. We need to implement this next.

```sql
CREATE TABLE ref_planets (planet_code VARCHAR(20) PRIMARY KEY, name VARCHAR(50));
CREATE TABLE ref_zodiac (sign_code VARCHAR(20) PRIMARY KEY, element VARCHAR(20), modality VARCHAR(20));
CREATE TABLE ref_traits (trait_code VARCHAR(50) PRIMARY KEY, category VARCHAR(20));

CREATE TABLE library_archetypes (
    archetype_id SERIAL PRIMARY KEY,
    planet_code VARCHAR(20) REFERENCES ref_planets(planet_code),
    sign_code VARCHAR(20) REFERENCES ref_zodiac(sign_code),
    variable_key VARCHAR(50),
    narrative_text TEXT,
    UNIQUE (planet_code, sign_code, variable_key)
);

CREATE TABLE library_wiring (
    wiring_id SERIAL PRIMARY KEY,
    variable_key VARCHAR(50),
    target_trait VARCHAR(50) REFERENCES ref_traits(trait_code),
    base_weight INT CHECK (base_weight BETWEEN -12 AND 12),
    UNIQUE (variable_key, target_trait)
);

CREATE TABLE characters (
    char_id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    level INT,
    age INT,
    bio TEXT
);

CREATE TABLE char_placements (
    placement_id SERIAL PRIMARY KEY,
    char_id INT REFERENCES characters(char_id) ON DELETE CASCADE,
    planet_code VARCHAR(20) REFERENCES ref_planets(planet_code),
    sign_code VARCHAR(20) REFERENCES ref_zodiac(sign_code),
    UNIQUE (char_id, planet_code)
);

CREATE TABLE char_resonance (
    resonance_id SERIAL PRIMARY KEY,
    char_id INT REFERENCES characters(char_id) ON DELETE CASCADE,
    planet_code VARCHAR(20) REFERENCES ref_planets(planet_code),
    volume INT DEFAULT 6 CHECK (volume BETWEEN 0 AND 12),
    UNIQUE (char_id, planet_code)
);
```

MY REQUEST: I have uploaded my current codebase (FULL_PROJECT_CONTEXT.txt). Please acknowledge the new Schema V2 plan. Our next step is to write a Migration Script to parse my existing archetype_text.py dictionary and populate these new SQL tables (library_archetypes and library_wiring) automatically.

---

### 🚀 Execution: Starting the New Chat

1.  Open a new Gemini window.
2.  **Prompt:** "Here is the full context for my Atomic Astrology project. I am uploading two things: 1. A summary of where we are going (Manifesto), and 2. My current codebase."
3.  **Paste** the "Handoff Manifesto" text above.
4.  **Upload/Drop** the `FULL_PROJECT_CONTEXT.txt` file.

The new Gemini will instantly be up to speed, ready to build the new database without needing you to explain "Evangelion Moon" or "1-12 Integers" again.
