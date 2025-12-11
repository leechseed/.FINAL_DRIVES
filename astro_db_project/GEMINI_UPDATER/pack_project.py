import os

# --- CONFIGURATION ---
# The path to your project folder
PROJECT_DIR = r"D:\.FINAL_DRIVES\astro_db_project"

# What file extensions do you want to include?
# Add ".sql" or ".md" if you have those files too.
INCLUDED_EXTENSIONS = [".py", ".sql", ".txt"]

# Files to explicitly ignore (like this script itself, or the output file)
IGNORE_FILES = ["pack_project.py", "FULL_PROJECT_CONTEXT.txt", "__pycache__"]

OUTPUT_FILE = "FULL_PROJECT_CONTEXT.txt"

def pack_project():
    print(f"📦 Scanning {PROJECT_DIR}...")
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
        # Write Header
        outfile.write("SYSTEM CONTEXT: ATOMIC ASTROLOGY PROJECT\n")
        outfile.write(f"Source Directory: {PROJECT_DIR}\n")
        outfile.write("="*60 + "\n\n")

        # Walk through the directory tree
        file_count = 0
        for root, dirs, files in os.walk(PROJECT_DIR):
            # Remove ignored directories from traversal
            dirs[:] = [d for d in dirs if d not in IGNORE_FILES]
            
            for file in files:
                if file in IGNORE_FILES:
                    continue
                
                # Check extension
                _, ext = os.path.splitext(file)
                if ext.lower() not in INCLUDED_EXTENSIONS:
                    continue

                # Construct full path
                full_path = os.path.join(root, file)
                # Create a relative path for cleaner reading (e.g., "scripts/logic.py")
                rel_path = os.path.relpath(full_path, PROJECT_DIR)

                print(f"   -> Packing {rel_path}")
                file_count += 1

                # Write File Start Header
                outfile.write(f"--- START FILE: {rel_path} ---\n")
                
                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as infile:
                        content = infile.read()
                        outfile.write(content)
                except Exception as e:
                    outfile.write(f"\n# ERROR READING FILE: {e}\n")
                
                # Write File End Footer
                outfile.write(f"\n--- END FILE: {rel_path} ---\n\n")

    print(f"\n✅ Done! Packed {file_count} files into '{OUTPUT_FILE}'.")
    print(f"You can now upload '{OUTPUT_FILE}' to a new Gemini chat.")

if __name__ == "__main__":
    pack_project()