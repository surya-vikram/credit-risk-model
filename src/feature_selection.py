import json
import pandas as pd
from scipy.stats import chi2_contingency, f_oneway
from statsmodels.stats.outliers_influence import variance_inflation_factor


def check_categorical_columns(df):
    return [col for col in df.columns if df[col].dtype == 'object' and col not in ['PROSPECTID', 'Approved_Flag']]


def chi_square_test(df, column_name):
    chi2, pval, _, _ = chi2_contingency(
        pd.crosstab(df[column_name], df['Approved_Flag']))
    return pval


def process_categorical_columns(df):
    categorical_columns = check_categorical_columns(df)
    for col in categorical_columns:
        p_value = chi_square_test(df, col)
        if p_value > 0.05:
            df = df.drop(col, axis=1)
    return df


def check_numeric_columns(df):
    return [col for col in df.columns if df[col].dtype != 'object' and col not in ['PROSPECTID', 'Approved_Flag']]


def calculate_vif(df):
    columns = check_numeric_columns(df)
    vif_data = df[columns]
    columns_to_be_removed = []
    for column in columns:
        vif_value = variance_inflation_factor(
            vif_data.values, vif_data.columns.get_loc(column))
        if vif_value > 6:
            columns_to_be_removed.append(column)
    return df.drop(columns=columns_to_be_removed)


def anova_test(df):
    columns = check_numeric_columns(df)
    for col in columns:
        groups = [df[col][df['Approved_Flag'] == level]
                  for level in df['Approved_Flag'].unique()]
        f_statistic, p_value = f_oneway(*groups)
        if p_value > 0.05:
            df.drop(col, axis=1)
    return df


def process_numerical_columns(df):
    df = calculate_vif(df)
    df = anova_test(df)
    return df


def process_dataframe(df):
    df = process_categorical_columns(df)
    df = process_numerical_columns(df)
    with open('column_names.json', 'w') as f:
        json.dump(df.columns.tolist(), f)
    return df
