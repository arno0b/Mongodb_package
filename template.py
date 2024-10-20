import os
from pathlib import Path
import logging

files=[
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",   #component of the pipeline
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_train.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "src/utils/utils.py",
    "tests/unit/__init__.py",   #testing each units
    "tests/integration/__init__.py",    #testing all units
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