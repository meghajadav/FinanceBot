import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

list_of_files= [
    'src/helper.py',
    'research/trials.py',
    'app.py',
    'src/prompt.py',
    'src/__init__.py',
    'app.py',
    'setup.py',
    'requirements.txt',
    '.env']

for file_path in list_of_files:
    file_path = Path(file_path)
    print(file_path)
    dir, file = os.path.split(file_path)
    if dir!="" :
        os.makedirs(dir, exist_ok=True)
        logging.info(f"creating directory {dir} for the {file}")
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,'w') as f:
            pass
            logging.info(f"creating file {file_path}")
    else:
        logging.info(f"{file_path} alreay exists")