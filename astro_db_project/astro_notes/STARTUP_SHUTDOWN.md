Here is the updated **`README_OPERATIONS.txt`** manual.

I have added a specific section (**STEP 0: AI CONTEXT REFRESH**) at the very top. This is the first thing you should run if you are opening a new chat window to continue coding.

Save this new version over your old file.

---

# 🚀 PROJECT OPERATIONS MANUAL

**Project:** Atomic Astrology Database
**Location:** `D:\.FINAL_DRIVES\astro_db_project`

---

## 🟢 PART 1: STARTUP PROCEDURE

_Perform this sequence when you sit down to work._

### STEP 0: AI CONTEXT REFRESH (If starting a new chat)

_Do this if you need to "teach" a new Gemini instance about your project._

1.  **Run the Packer:**
    ```bash
    python GEMINI_UPDATER\pack_project.py
    ```
2.  **Locate the File:** Go to `D:\.FINAL_DRIVES\astro_db_project\GEMINI_UPDATER`.
3.  **Upload:** Drag and drop `FULL_PROJECT_CONTEXT.txt` into the chat window.
4.  **Verification:** The AI should confirm it understands the "Eva/GTA" tone and the "Weighted Sum" math.

### STEP 1: Open the Terminal & Navigate

Open Command Prompt (or PowerShell) and go to your project root.

```bash
cd D:\.FINAL_DRIVES\astro_db_project
```

### STEP 2: Activate the Virtual Environment (Sandbox)

Turn on the safe mode where your libraries live.

```bash
venv\Scripts\activate
```

- **Verification:** You should see `(venv)` in green/white at the start of your command line.
  - _If you don't see it:_ You are not in the sandbox. Run `python -m venv venv` to rebuild it.

### STEP 3: Ensure Database is Awake

PostgreSQL usually runs in the background, but let's verify it's listening.

- **Action:** Run your wiring script. This tests the connection _and_ updates any code changes you made last time.

<!-- end list -->

```bash
python map_bfas.py
```

- **Verification:** Look for the message: `✅ BFAS Wiring Complete`.
  - _If it fails:_ Your Postgres server is likely off. Open "Services" in Windows and start `postgresql-x64-16`.

### STEP 4: Run the Logic Engine (The Refresh)

Recalculate all character stats based on the latest 1-12 settings.

```bash
python astro_logic.py
```

- **Verification:** Look for the final line: `✅ SYSTEM: All Systems synced. The engine is hot.`

### STEP 5: Launch the Visualizer

Start the web dashboard.

```bash
streamlit run app.py
```

- **Verification:** A browser tab will open automatically to `http://localhost:8501`.
- **Visual Check:** You should see "⚛️ Atomic Astrology: The Soul Tuner" and the mixing board sliders.

---

## 🔴 PART 2: SHUTDOWN PROCEDURE

_Perform this sequence when you are done for the day._

### Step 1: Stop the Visualizer

Go to the terminal where Streamlit is running.

- **Action:** Press `Ctrl + C` on your keyboard.
- **Verification:** The terminal should return to the command prompt (e.g., `(venv) D:\...>`).

### Step 2: Deactivate the Sandbox

Exit the virtual environment.

```bash
deactivate
```

- **Verification:** The `(venv)` prefix will disappear from your command line.

### Step 3: Close Terminal

Simply close the window. Your database (Postgres) is safe to stay running in the background; it uses minimal resources when idle.

---

## 🛠️ PART 3: TROUBLESHOOTING & VERIFICATION LIST

If "shit isn't running," run these checks in order:

**1. "I changed the weights but the graph didn't move."**

- **Cause:** The Database mapping table is stale.
- **Fix:** Run `python map_bfas.py`, then `python astro_logic.py`.

**2. "Streamlit says 'Module not found'."**

- **Cause:** You forgot to activate the venv.
- **Fix:** Close terminal, re-open, run `venv\Scripts\activate`.

**3. "Database Connection Refused."**

- **Cause:** Postgres Service is down or password changed.
- **Fix:** Check `DB_CONFIG` in your python files. It should match your Postgres setup (Port 5433).

**4. "The text descriptions are missing in the dashboard."**

- **Cause:** You edited `archetype_text.py` but didn't push it to the DB.
- **Fix:** Run `python update_system.py`.
