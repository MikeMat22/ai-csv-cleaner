# AI CSV Cleaner & Analyzer

A Streamlit app for analyzing and cleaning CSV datasets. Useful for data preparation before machine learning.

## Features

**Dataset Analysis**
- Row and column count overview
- Data type detection
- Missing value identification
- Duplicate row count
- Empty column detection
- Statistics for numeric columns

**Dataset Cleaning**
- Remove duplicate rows
- Remove empty columns
- Auto-fill missing values (median for numbers, "unknown" for text)
- Label column normalization (scam/spam/fraud → 1, ham/legit → 0)
- Export cleaned dataset as CSV

## Installation

```bash
git clone https://github.com/MikeMat22/ai-csv-cleaner.git
cd ai-csv-cleaner

python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

The app runs at `http://localhost:8501`.

## Project Structure

```
├── app.py              # Main Streamlit app
├── analyzer.py         # Dataset analysis module
├── cleaner.py          # Dataset cleaning module
├── requirements.txt    # Python dependencies
├── messy_customers.csv # Sample dataset
└── messy_scam_messages.csv # Sample dataset
```

## License

MIT
