import pandas as pd

def analyze_dataframe(df: pd.DataFrame) -> dict:
    report = {}

    # Basic shape
    report["rows"] = df.shape[0]
    report["columns"] = df.shape[1]

    # Column names
    report["column_names"] = df.columns.tolist()

    # Data types
    report["dtypes"] = df.dtypes.astype(str).to_dict()

    # Missing values
    report["missing_values"] = df.isnull().sum().to_dict()

    # Duplicate rows
    report["duplicate_rows"] = int(df.duplicated().sum())

    # Empty columns (all NaN)
    report["empty_columns"] = df.columns[df.isnull().all()].tolist()

    # Basic statistics for numeric columns
    numeric_df = df.select_dtypes(include="number")
    if not numeric_df.empty:
        report["numeric_stats"] = numeric_df.describe().to_dict()
    else:
        report["numeric_stats"] = {}

    return report