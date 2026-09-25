from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

path = Path()

APP = os.getenv("APP")
CWD = path.cwd()
DATA = CWD / os.getenv("DATA_FOLDER")
MEMBERS_FILE = DATA / os.getenv("MEMBERS_FILE")
MEMBERSHIPS_FILE = DATA / os.getenv("MEMBERSHIPS_FILE")
CITIES = os.getenv("CITIES").split(",")

print(MEMBERS_FILE, MEMBERSHIPS_FILE)
