import pandas as pd
from config import PROCESSED_DATA_DIR
from config import RAW_DATA_DIR
from data_inspection import columns_to_check

# Load dataset
df = pd.read_csv(RAW_DATA_DIR / "mp_Li_O_containing.csv")

# Creating the clean DataSet and plancing it in Processed Data
# Remove duplicates, keeping one material per group
df_clean = df.drop_duplicates(
    subset=columns_to_check,
    keep='first'
).copy()

# Save cleaned dataset
df_clean.to_csv(
    PROCESSED_DATA_DIR / "mp_Li_O_clean.csv",
    index=False
)

print(f"\nOriginal dataset: {len(df)} materials")
print(f"Cleaned dataset: {len(df_clean)} materials")
print(f"Duplicates removed: {len(df) - len(df_clean)}")