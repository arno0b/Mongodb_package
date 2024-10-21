import os
from pathlib import Path
import logging

package= "mongodb_connect"
files=[
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    f"src/{package}/__init__.py",   #component of the pipeline
    f"src/{package}/mongo_crud.py",
    "src/utils/utils.py",
    "tests/unit/__init__.py",
    "tests/unit/unit.py",   #testing each units
    "tests/integration/__init__.py",    #testing all units
    "tests/integration/int.py", 
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.cfg",
    "setup.py",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]

for file_path in files:
    file_path=Path(file_path)
    file_dir, filename = os.path.split(file_path)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating direction: {file_dir} for file: {filename}")
    if(not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass