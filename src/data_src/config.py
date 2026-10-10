import os
from pathlib import Path
from dotenv import load_dotenv

# Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Data directories
RAW_DATA_DIR = BASE_DIR / "data" / "raw"

# Create directory if it does not exist
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Load Materials Project API key from .env
load_dotenv(BASE_DIR / ".env")
MP_API_KEY = os.getenv("MP_API_KEY")

if not MP_API_KEY:
    raise ValueError("Materials Project API key not found in .env!")

print("Materials Project API key loaded successfully")
print("Setup complete!")