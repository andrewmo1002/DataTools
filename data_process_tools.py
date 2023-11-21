import pandas as pd
import numpy as np
import datetime


def categorize_columns(dataframe):
    numeric_cols = dataframe.select_dtypes(include=[np.number]).columns.tolist()
    object_cols = dataframe.select_dtypes(include=[object]).columns.tolist()
    datetime_cols = dataframe.select_dtypes(include=[np.datetime64]).columns.tolist()
    bool_cols = dataframe.select_dtypes(include=[bool]).columns.tolist()
    other_cols = dataframe.select_dtypes(exclude=[np.number, np.datetime64, bool, object]).columns.tolist()

    return {
        'numeric': numeric_cols,
        'object': object_cols,
        'datetime': datetime_cols,
        'bool': bool_cols,
        'other': other_cols
    }


def data_cleaning(df, method="drop"):
    if method == "drop":
        df.dropna(axis=0, how="any", inplace=True)
    elif method == "ffill":
        if df.isna().values.any():
            df.fillna(method='ffill', inplace=True)
            df.fillna(method='backfill', inplace=True)
            df.fillna(0, inplace=True)
    elif method == "backfill":
        if df.isna().values.any():
            df.fillna(method='backfill', inplace=True)
            df.fillna(method='ffill', inplace=True)
            df.fillna(0, inplace=True)
    return df
