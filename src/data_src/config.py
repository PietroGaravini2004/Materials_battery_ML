import os
from pathlib import Path
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
from datetime import datetime

# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load API key from .env
load_dotenv(BASE_DIR / ".env")
MP_API_KEY = os.getenv("MP_API_KEY")

if not MP_API_KEY:
    raise ValueError("Materials Project API key not found!")

print("✓ Materials Project API key loaded successfully")

# Plot settings
sns.set_theme(style="whitegrid")
plt.rcParams.update({"figure.dpi": 120})

# Create data directory
(BASE_DIR / "data" / "raw").mkdir(parents=True, exist_ok=True)

print("Setup complete!")