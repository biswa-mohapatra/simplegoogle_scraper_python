import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format= "[%(asctime)s: %(levelname)s] : %(message)s"
)

while True:
    project_name = input("Enter the project name: ")
    if project_name != "":
        break

logging.info(f"Creating project by name: {project_name}")

# list of files:
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    "tests/__init__.py",
    "init_setup.sh",
    "requirements_dev.txt",
    "requirements.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini",
]

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory at: {filedir} for file: {filename}")
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path,"w") as f:
            pass
            logging.info(f"Creating a new file: {filename} at path: {file_path}")
    else:
        logging.info(f"File is already exist at: {file_path}")