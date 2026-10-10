from pathlib import Path
import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parents[1]

# importing the csv file of raw data
df = pd.read_csv(BASE_DIR / "data" / "raw" / "mp_Li_O_containing.csv")

# visualizations settings
st.title("Materials Project — Raw Dataset")
st.write(f"Dimensions: {df.shape[0]} rows × {df.shape[1]} columns")
st.dataframe(df, width="stretch", height=650)