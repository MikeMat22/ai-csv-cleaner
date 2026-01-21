import pandas as pd
import numpy as np
from typing import Optional

LABEL_MAP = {
    "scam": 1,
    "spam": 1,
    "fraud": 1,
    "1": 1,
    1: 1,
    "ham": 0,
    "legit": 0,
    "not scam": 0,
    "0": 0,
    0: 0
}

def clean_dataframe(df: pd.DataFrame, label_column: Optional[str] = None):
    log = []

    # Copy to avoid mutating original
    cleaned_df = df.copy()

    # Drop duplicate rows
    dup_count = cleaned_df.duplicated().sum()
    if dup_count > 0:
        cleaned_df = cleaned_df.drop_duplicates()
        log.append(f"Removed {dup_count} duplicate rows")

    # Drop empty columns
    empty_cols = cleaned_df.columns[cleaned_df.isnull().all()].tolist()
    if empty_cols:
        cleaned_df = cleaned_df.drop(columns=empty_cols)
        log.append(f"Dropped empty columns: {empty_cols}")

    # Fill missing values
    for col in cleaned_df.columns:
        if cleaned_df[col].isnull().any():
            if cleaned_df[col].dtype in ["int64", "float64"]:
                median = cleaned_df[col].median()
                cleaned_df[col] = cleaned_df[col].fillna(median)
                log.append(f"Filled NaN in '{col}' with median ({median})")
            else:
                cleaned_df[col] = cleaned_df[col].fillna("unknown")
                log.append(f"Filled NaN in '{col}' with 'unknown'")

    # Normalize labels (if provided)
    if label_column and label_column in cleaned_df.columns:
        cleaned_df[label_column] = (
            cleaned_df[label_column]
            .astype(str)
            .str.lower()
            .map(LABEL_MAP)
        )
        cleaned_df = cleaned_df.dropna(subset=[label_column])
        log.append(f"Normalized label column '{label_column}'")

    return cleaned_df, log