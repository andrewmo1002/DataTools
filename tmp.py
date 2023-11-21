    def data_cleaning(self, df, method="drop"):
        if method == "drop":
            df.dropna(axis=0, how="any", inplace=True)
        elif method == "ffill":
            if df.isna().values.any():
                # 用前一行、后一行的数据来填充NaN值
                df.fillna(method='ffill', inplace=True)
                df.fillna(method='backfill', inplace=True)
                # 用0填充NaN值
                df.fillna(0, inplace=True)
        elif method == "backfill":
            if df.isna().values.any():
                # 用前一行、后一行的数据来填充NaN值
                df.fillna(method='backfill', inplace=True)
                df.fillna(method='ffill', inplace=True)
                # 用0填充NaN值
                df.fillna(0, inplace=True)
        return df