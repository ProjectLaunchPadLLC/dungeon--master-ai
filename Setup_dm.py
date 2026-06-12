import os
import json

def setup_repository():
    # Define the structure: {path: content}
    # None indicates a folder
    structure = {
        "docs": None,
        "product": None,
        "constraints": None,
        "execution": None,
        "quality": None,
        "skills": None,
        "src": None,
        "src/engine.py": "# Main AI DM execution loop goes here.",
        "src/state.py": "# JSON handling and persistent storage logic.",
        "src/github_io.py": "# GitHub Gist/Repository communication logic.",
        "FOUNDATION.md": "# System Directive\nYou are the Dungeon Master...",
        "PICKUP.md": json.dumps({"session": "initialized", "data": {}}, indent=4),
        "README.md": "# Dungeon Master AI\nCustom AI engine for D&D."
    }

    print("Initializing Dungeon Master AI Repository...")

    for path, content in structure.items():
        if content is None:
            # Create directory
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"Created folder: {path}")
        else:
            # Create file
            with open(path, 'w') as f:
                f.write(content)
                print(f"Created file: {path}")

    print("\nRepository setup complete.")

if __name__ == "__main__":
    setup_repository()
