import streamlit as st
import pandas as pd
import plotly.express as px
import pg8000.native
import astro_logic  # Imports your logic engine to recalculate stats on the fly

# --- CONFIGURATION ---
DB_CONFIG = {
    "database": "atomic_astro_db",
    "user": "postgres",
    "password": "C970D6567B7724E907EF0F8CE4A2C9E1",
    "host": "localhost",
    "port": 5433
}

# --- DATABASE FUNCTIONS ---
def get_connection():
    return pg8000.native.Connection(**DB_CONFIG)

def get_characters():
    conn = get_connection()
    df = pd.DataFrame(conn.run("SELECT char_id, name, archetype, level FROM characters"), 
                      columns=['ID', 'Name', 'Archetype', 'Level'])
    conn.close()
    return df

def get_bfas_scores(char_id):
    conn = get_connection()
    df = pd.DataFrame(conn.run("""
        SELECT trait_name, score FROM bfas_scores WHERE char_id = :cid
    """, cid=char_id), columns=['Trait', 'Score'])
    conn.close()
    return df

def get_resonance(char_id):
    conn = get_connection()
    # Pulls the current volume (or defaults to 6 if null) and the narrative description
    data = conn.run("""
        SELECT 
            s.subsystem_code, 
            COALESCE(r.volume, 6) as volume,
            n.title,
            n.description
        FROM subsystems s
        LEFT JOIN character_resonance r ON s.subsystem_code = r.subsystem_code AND r.char_id = :cid
        LEFT JOIN narrative_definitions n ON s.subsystem_code = n.context_code
        WHERE s.subsystem_code IN 
            ('SUN', 'MOON', 'MERCURY', 'VENUS', 'MARS', 'JUPITER', 'SATURN', 'URANUS', 'NEPTUNE', 'PLUTO')
    """, cid=char_id)
    conn.close()
    
    # Structure for easy access
    res_map = {}
    for row in data:
        code = row[0]
        res_map[code] = {
            'volume': row[1],
            'title': row[2] if row[2] else code,
            'desc': row[3] if row[3] else "No description available."
        }
    return res_map

def update_db_resonance(char_id, planet, new_vol):
    conn = get_connection()
    conn.run("""
        INSERT INTO character_resonance (char_id, subsystem_code, volume)
        VALUES (:cid, :sub, :vol)
        ON CONFLICT (char_id, subsystem_code) 
        DO UPDATE SET volume = :vol
    """, cid=char_id, sub=planet, vol=new_vol)
    conn.close()
    
    # TRIGGER THE LOGIC ENGINE!
    # This recalculates the stats immediately so the chart updates.
    conn = get_connection()
    astro_logic.calculate_bfas_scores(conn)
    conn.close()

# --- UI LAYOUT ---
st.set_page_config(page_title="Atomic Astro Tuner", layout="wide")

st.title("⚛️ Atomic Astrology: The Soul Tuner")
st.markdown("Adjust the **Resonance Volumes** (1-12) to see how psychological integration changes the personality stats.")

# 1. SIDEBAR: Character Select
st.sidebar.header("Select Subject")
chars = get_characters()
selected_char_name = st.sidebar.selectbox("Character", chars['Name'])
char_id = int(chars[chars['Name'] == selected_char_name]['ID'].values[0])
char_arch = chars[chars['Name'] == selected_char_name]['Archetype'].values[0]

st.sidebar.markdown(f"**ID:** {char_id} | **Arch:** {char_arch}")

# 2. LOAD DATA
scores_df = get_bfas_scores(char_id)
resonance_data = get_resonance(char_id)

# 3. TOP ROW: Visualizer & Tuner
col_chart, col_tuner = st.columns([2, 1])

with col_chart:
    st.subheader(f"🧠 Psychometric Radar: {selected_char_name}")
    
    if not scores_df.empty:
        # Create Spider Graph
        fig = px.line_polar(scores_df, r='Score', theta='Trait', line_close=True,
                            range_r=[0, 60], markers=True)
        fig.update_traces(fill='toself', line_color='#00CC96')
        fig.update_layout(polar=dict(radialaxis=dict(visible=True)), showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No stats calculated yet. Run the Logic Engine.")

with col_tuner:
    st.subheader("🎛️ Resonance Mixing Board")
    st.markdown("_Volume 1 (Trace) to 12 (Dominant)_")
    
    # Create a slider for each planet
    # We define the order we want them to appear
    planet_order = ['SUN', 'MOON', 'MERCURY', 'VENUS', 'MARS', 'SATURN', 'JUPITER', 'URANUS', 'NEPTUNE', 'PLUTO']
    
    for planet in planet_order:
        data = resonance_data.get(planet, {'volume': 6, 'title': planet, 'desc': ''})
        
        # Display the slider
        # key=planet ensures Streamlit knows which slider is which
        new_val = st.slider(f"{planet} ({data['title']})", 1, 12, value=data['volume'], key=planet)
        
        # If slider moved, update DB and rerun
        if new_val != data['volume']:
            update_db_resonance(char_id, planet, new_val)
            st.rerun() # Refresh the page to show new stats

# 4. BOTTOM ROW: Narrative Context (The "Consultant's Roundup")
st.markdown("---")
st.subheader("📚 Narrative Context (The Consultant's Notes)")

# Create 3 columns for better readability of the text
cols = st.columns(3)
for i, planet in enumerate(planet_order):
    data = resonance_data.get(planet, {})
    col_idx = i % 3
    with cols[col_idx]:
        st.markdown(f"#### **{planet}: {data.get('title', '')}**")
        st.caption(data.get('desc', 'No data.'))
        st.markdown("---")