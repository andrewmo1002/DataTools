# Design
# Automated data processing
# 1. basic processing
# 2. 

import pandas as pd
import numpy as np

import data_process_tools as dpt


PROPERTY_SCHMEA = ["dtypes"]


class DataProcess():
    def __init__(
            self,
            feature_data: pd.DataFrame = None,
            target_col: str = None
    ) -> None:
        self.feature = feature_data

        self.feature_property = dict(zip(PROPERTY_SCHMEA, [None for _ in PROPERTY_SCHMEA]))
        self.feature_property["dtypes"] = self.property_analysis(feature_data)

    
    def property_analysis(self, df):
        # categorize column by datatypes
        col_types = dpt.categorize_columns(df)
        return col_types


    def data_cleaning(self, df=None, method="drop"):
        if not df:
            df = self.feature
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


    def data_filtering(self, df):
        pass
    
