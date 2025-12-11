Yes, absolutely. The entire architecture we just built is designed specifically for that kind of modularity.

In this "Atomic" system, a **Custom Overlay** (like a specific magic system from a book, a cybernetic implant list, or a faction allegiance) is treated exactly the same way as a Planet. It is just another "layer" of tags that gets added to the calculation pile.

Here is exactly how you would add a custom system (e.g., **"The Dune Factions"**) later without breaking anything.

### The 3-Step Process for Custom Overlays

#### 1\. Create the Data File (`overlay_dune.py`)

You define your new variables just like you did for the Zodiac.

```python
# overlay_dune.py
FACTION_DATA = {
    "ATREIDES": {
        "lore": "Noble, dutiful, and arrogant.",
        "variables": {
            "FACTION_CODE": "Atreides Honor",
            "TRAINING_STYLE": "Mentat Logic"
        }
    },
    "HARKONNEN": {
        "lore": "Brutal, industrial, and cunning.",
        "variables": {
            "FACTION_CODE": "Harkonnen Ambition",
            "TRAINING_STYLE": "Torture Conditioning"
        }
    }
}
```

#### 2\. Create the Wiring (`map_dune.py`)

You tell the engine how these new tags affect the BFAS stats.

```python
# map_dune.py
def wire_dune():
    # Atreides adds to Industriousness (Duty)
    add_mapping("Atreides Honor", "Industriousness", 1.5)

    # Harkonnen adds to Assertiveness (Brutality)
    add_mapping("Harkonnen Ambition", "Assertiveness", 2.0)
```

#### 3\. Update the Engine (`astro_logic.py`)

You just add one line to your master script to "plug in" the new module.

```python
# In astro_logic.py
import map_dune  # <--- New Import

def refresh_all_logic():
    # ... existing wires ...
    map_dune.wire_dune() # <--- New Wiring Call
    calculate_bfas_scores()
```

### Why this is safe

Because the math is **Additive**, the new system doesn't overwrite the old one; it simply adds new "rocks" to the bucket.

- **Character A:**
  - **Sun:** Aries (+1 Assertiveness)
  - **Overlay:** Harkonnen (+2 Assertiveness)
  - **Total:** 3.0 Assertiveness

You can add, remove, or swap these overlays endlessly. You could have a character who is an **Aries / Harkonnen / Jedi**, and the math would simply stack up to create a very intense, high-conflict personality.
