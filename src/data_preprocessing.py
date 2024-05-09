import pandas as pd
from pathlib import Path


def load_data():
    current_path = Path(__file__).resolve()
    root_path = current_path.parent.parent
    internal_df_path = root_path / 'data' / 'internal.xlsx'
    external_df_path = root_path / 'data' / 'external.xlsx'

    try:
        internal_df = pd.read_excel(internal_df_path)
        external_df = pd.read_excel(external_df_path)
    except FileNotFoundError:
        raise FileNotFoundError(
            "Data file not found. Please check the file path.")
    except Exception as e:
        raise Exception("Error reading data file:", e)

    return internal_df, external_df


def remove_nulls(df1, df2):
    df1 = df1[df1['Age_Oldest_TL'] != -99999]
    columns_to_be_removed = [
        col for col in df2.columns if df2[col].eq(-99999).sum() > 10000]
    df2 = df2.drop(columns=columns_to_be_removed)
    df2 = df2[~df2.isin([-99999]).any(axis=1)]
    return df1, df2


def merge_dataframes(df1, df2):
    df = pd.merge(df1, df2, how='inner', on='PROSPECTID')
    return df

