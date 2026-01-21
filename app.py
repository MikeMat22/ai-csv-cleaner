import streamlit as st
import pandas as pd

from analyzer import analyze_dataframe
from cleaner import clean_dataframe

st.set_page_config(
    page_title="AI CSV Cleaner & Analyzer",
    layout="wide"
)

st.title("🧠 AI CSV Cleaner & Analyzer")

uploaded_file = st.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # =======================
    # PREVIEW
    # =======================
    st.subheader("Preview")
    st.dataframe(df.head())

    # =======================
    # ANALYZER
    # =======================
    if st.button("Analyze dataset"):
        report = analyze_dataframe(df)

        st.subheader("Dataset overview")
        st.write(f"Rows: {report['rows']}")
        st.write(f"Columns: {report['columns']}")

        st.subheader("Column types")
        st.json(report["dtypes"])

        st.subheader("Missing values per column")
        st.json(report["missing_values"])

        st.subheader("Duplicate rows")
        st.write(report["duplicate_rows"])

        if report["empty_columns"]:
            st.subheader("Empty columns")
            st.write(report["empty_columns"])

        if report["numeric_stats"]:
            st.subheader("Numeric statistics")
            st.json(report["numeric_stats"])

    # =======================
    # CLEANER
    # =======================
    st.subheader("🧼 Clean dataset")

    label_column = st.text_input(
        "Optional: name of label column (e.g. label, scam, target)"
    )

    if st.button("Clean dataset"):
        cleaned_df, log = clean_dataframe(
            df,
            label_column or None
        )

        st.success("Dataset cleaned successfully")

        st.subheader("Cleaning log")
        for item in log:
            st.write("•", item)

        st.subheader("Cleaned preview")
        st.dataframe(cleaned_df.head())

        csv = cleaned_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇️ Download cleaned CSV",
            csv,
            file_name="cleaned_dataset.csv",
            mime="text/csv"
        )
        