import pandas as pd
import numpy as np

import pandas as pd

def load_dataset(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    return df


def remove_outliers(df):
    # IQR Method
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1

    df_clean = df[~((df < (Q1 - 1.5 * IQR)) | 
                    (df > (Q3 + 1.5 * IQR))).any(axis=1)]
    return df_clean

def split_features_labels(df):
    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]
    return X, y

def replace_zero_with_median(df):
    cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    for col in cols:
        df[col] = df[col].replace(0, df[col].median())
    return df

