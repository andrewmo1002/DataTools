# Goal of this script:
# Provide an automated tool for quick and preliminary data analysis
# Provide data processing and data analysis tools for further operations

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import data_process_tools as dpt
import data_analysis_tools as dat


PROPERTY_SCHMEA = ["dtypes", "mean", "std_values"]


class DataAnalysis():
    def __init__(self, feature_data: pd.DataFrame = None, target_col = None) -> None:
        self.feature = feature_data
        self.property = dict(zip(PROPERTY_SCHMEA, [None for _ in PROPERTY_SCHMEA]))
        self.report_msg("initializing")
        self.run()


    def run(self):
        self.data_cleaning()
        self.data_filtering()
        self.property_analysis()
        self.statistics_analysis()

        self.report_msg("running ends")


    def data_cleaning(self, method="drop"):
        self.report_msg("data cleaning starts")

        dpt.data_cleaning(self.feature, method)
        
        self.report_msg("data cleaning ends")
        # return df


    def data_filtering(self):
        # TODO: finish custom filtering here
        # print("Data filtering")
        # self.feature
        pass

    
    def property_analysis(self):
        # categorize column by datatypes
        self.property["dtypes"] = dpt.categorize_columns(self.feature)
        self.report_msg("property analysis ends")


    def statistics_analysis(self):
        self.report_msg("statistics analysis starts")
        # 1. mean, std
        mean_values = self.feature.mean(numeric_only=True)
        std_values = self.feature.std(numeric_only=True)
        self.property["mean"] = mean_values
        self.property["std_values"] = std_values
        # 2. ...
    

    def visual_distribution(self):
        if len(self.property["dtypes"]['numeric']) > 0:
            dat.visual_distribution(
                df=self.feature,
                mean_values=self.property["mean"],
                std_values=self.property["std_values"]
            )

    
    def report_msg(self, position):

        if position == "initializing":
            print("Instance initiated. Running...")
            print()

        elif position == "running ends":
            print("Run Completed")
            # 1. Property Reporrt
            print("    Property created: ", end="")
            for key in self.property:
                print(f"{key}, ", end="")
            print()

            # 2. Visual Tools report
            print("    Visual options: ")
            print("        .visual_distribution()")

        elif position == "data cleaning starts":
            print("Data cleaning...")
            print(f"    before: {self.feature.shape}")

        elif position == "data cleaning ends":
            print(f"    after: {self.feature.shape}")
            print()

        elif position == "property analysis ends":
            print("Basic property checking...")
            print("    column dtypes: ", end="")
            for key in self.property["dtypes"]:
                print(f"{key}: {len(self.property['dtypes'][key])}", end=", ")
            print(end=2*'\n')

        elif position == "statistics analysis starts":
            print("Calculating data statistics...")
            print()
