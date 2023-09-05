import os

HOME_DIR = os.path.realpath(os.path.abspath(os.curdir))
DATA_DIR = os.path.realpath(os.path.join(HOME_DIR, "data"))
SRC_DIR = os.path.realpath(os.path.join(HOME_DIR, "src"))
TEST_DIR = os.path.realpath(os.path.join(HOME_DIR, "tests"))

PHTOTOS_INPUT = os.path.realpath(os.path.join(DATA_DIR, "input"))
PHTOTOS_OUTPUT = os.path.realpath(os.path.join(DATA_DIR, "output"))

check_folders = [DATA_DIR, PHTOTOS_INPUT, PHTOTOS_OUTPUT]

for folder in check_folders:
    if not os.path.exists(folder):
        os.mkdir(folder)
