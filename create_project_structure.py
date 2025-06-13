import os
from pathlib import Path

def create_directory(path):
    Path(path).mkdir(parents=True, exist_ok=True)
    print(f"✓ Created directory: {path}")

def create_file(filepath, content=""):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Created file: {filepath}")

def create_project_structure(base_path="."):
    base = Path(base_path)
    directories = [
        base / ".vscode",
        base / ".github" / "workflows",
        base / "src" / "core",
        base / "src" / "models",
        base / "src" / "utils",
        base / "src" / "services",
        base / "tests" / "unit",
        base / "tests" / "integration",
        base / "notebooks",
        base / "scripts",
        base / "docs",
        base / "data" / "raw",
        base / "data" / "processed",
        base / "config",
        base / "examples"
    ]
    for d in directories:
        create_directory(d)
    init_files = [
        base / "src" / "__init__.py",
        base / "src" / "core" / "__init__.py",
        base / "src" / "models" / "__init__.py",
        base / "src" / "utils" / "__init__.py",
        base / "src" / "services" / "__init__.py",
        base / "tests" / "__init__.py",
        base / "tests" / "unit" / "__init__.py",
        base / "tests" / "integration" / "__init__.py",
        base / "notebooks" / "__init__.py",
        base / "scripts" / "__init__.py",
        base / "config" / "__init__.py",
        base / "examples" / "__init__.py"
    ]
    for f in init_files:
        create_file(f, '"""Package initialization file."""\n')
    files = [
        (base / ".gitignore", "__pycache__/\n*.pyc\n.venv/\n.env\n"),
        (base / "requirements.txt", "# Add your dependencies here\nnumpy\npandas\n"),
        (base / "README.md", "# Project Title\n\nDescribe your project here."),
        (base / "pyproject.toml", "[build-system]\nrequires = [\"setuptools>=42\"]\nbuild-backend = \"setuptools.build_meta\"\n"),
        (base / ".vscode" / "settings.json", "{\"python.defaultInterpreterPath\": \"./venv/Scripts/python.exe\"}"),
        (base / ".github" / "workflows" / "ci.yml", "name: Python package\n\non: [push]\n\njobs:\n  build:\n    runs-on: ubuntu-latest\n    steps:\n    - uses: actions/checkout@v2\n    - name: Set up Python\n      uses: actions/setup-python@v2\n      with:\n        python-version: '3.x'\n    - name: Install dependencies\n      run: |\n        python -m pip install --upgrade pip\n        pip install -r requirements.txt\n    - name: Run tests\n      run: |\n        pytest\n"),
        (base / "Makefile", "install:\n\tpip install -r requirements.txt\n"),
        (base / "docs" / "README.md", "# Documentation\n"),
        (base / "notebooks" / "README.md", "# Notebooks\n"),
        (base / "scripts" / "README.md", "# Scripts\n"),
        (base / "data" / "README.md", "# Data directory\n"),
        (base / "examples" / "README.md", "# Examples\n"),
        (base / "config" / "settings.py", "# Configuration settings\n")
    ]
    for f, c in files:
        create_file(f, c)
    print("✅ Project structure created!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        create_project_structure(sys.argv[1])
    else:
        create_project_structure()
