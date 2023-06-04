import os


def create_directory_structure(base_path):
    directories = ["", "evolution_simulation", "tests", "examples", "docs"]

    files = [
        ".gitignore",
        "README.md",
        "setup.py",
        "requirements.txt",
        "evolution_simulation/__init__.py",
        "evolution_simulation/organisms.py",
        "evolution_simulation/environment.py",
        "evolution_simulation/genetics.py",
        "evolution_simulation/simulation.py",
        "evolution_simulation/visualization.py",
        "tests/__init__.py",
        "tests/test_organisms.py",
        "tests/test_environment.py",
        "tests/test_genetics.py",
        "tests/test_simulation.py",
        "examples/simple_simulation.py",
        "examples/complex_simulation.py",
        "docs/index.md",
        "docs/installation.md",
        "docs/usage.md",
        "docs/api.md",
    ]

    for directory in directories:
        os.makedirs(os.path.join(base_path, directory), exist_ok=True)

    for file in files:
        with open(os.path.join(base_path, file), "w") as fp:
            pass  # Just create the file


create_directory_structure("evolution_simulation")
