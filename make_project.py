import os

def create_project_structure(base_path):
    # Define the project structure
    structure = {
        "app.py": "",
        "templates": {
            "base.html": "",
            "home.html": "",
            "game1.html": "",
            "game2.html": ""
        },
        "static": {
            "css": {
                "styles.css": ""
            },
            "js": {
                "scripts.js": ""
            }
        },
        "games": {
            "game1.py": "",
            "game2.py": ""
        }
    }

    # Recursive function to create directories and files
    def create_structure(path, elements):
        if isinstance(elements, dict):
            for name, content in elements.items():
                new_path = os.path.join(path, name)
                if isinstance(content, dict):
                    os.makedirs(new_path, exist_ok=True)
                    create_structure(new_path, content)
                else:
                    with open(new_path, 'w') as f:
                        f.write(content)

    # Create the base directory
    os.makedirs(base_path, exist_ok=True)

    # Create the project structure
    create_structure(base_path, structure)

# Specify the base path for the project
base_path = "game_platform"
create_project_structure(base_path)
