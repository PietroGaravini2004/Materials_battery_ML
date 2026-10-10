import pandas as pd
import numpy as np
import os
from config import RAW_DATA_DIR
from scipy import stats


# Load dataset
df = pd.read_csv(RAW_DATA_DIR / "mp_Li_O_containing.csv")

# Dataset dimensions
print(f"Dataset dimensions: {df.shape}")

# Check of the missing values
missing_values = df.isnull().sum()
print("Missing values per column:")
print(missing_values)

# Check of the duplicates
columns_to_check = df.columns.drop("material_id")

duplicates_groups = (
    df.groupby(list(columns_to_check), dropna=False)
    .size()
    .reset_index(name="count")
)

duplicates_groups = duplicates_groups[
    duplicates_groups["count"] > 1
]

duplicates_groups = duplicates_groups.sort_values(
    "count", ascending=False
)
total_duplicates_to_delete = (duplicates_groups["count"] - 1).sum()

print(f"Total duplicated materials: {total_duplicates_to_delete}")
print(duplicates_groups[["formula", "count"]].to_string(index=False))

# Printing one group of duplicates
group = duplicates_groups.iloc[0]
mask = df[columns_to_check].eq(group[columns_to_check]).all(axis=1)
print(df[mask].to_string())

# Outlier detection with Z score > 3
print('Outlier detection (|z| > 3):')
for col in ['Ef','Ehull','Eg','volume_per_site']:
    d = df[col].dropna()
    z = np.abs(stats.zscore(d))
    n_out = (z > 3).sum()
    print(f'  {col:20s}: {n_out:4d} outliers ({100*n_out/len(d):.1f}%)')
    df[f'{col}_outlier'] = False
    df.loc[d.index[z > 3], f'{col}_outlier'] = True
print('\nOutliers FLAGGED (not removed) — they may be genuine extreme cases.')