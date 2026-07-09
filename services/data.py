import pandas as pd


def clean_value(value):

    if pd.isna(value):
        return "N/A"

    return str(value).strip()


def row_to_text(row):

    parts = []

    for column, value in row.items():

        clean_column = str(column).strip().lower()
        clean_data = clean_value(value)

        parts.append(f"{clean_column}: {clean_data}")

    return " | ".join(parts)


def process_csv(file):

    df = pd.read_csv(file)

    documents = []

    for _, row in df.iterrows():

        content = row_to_text(row)

        documents.append(content)

    return documents