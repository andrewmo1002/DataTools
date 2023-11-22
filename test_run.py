import pandas as pd
import numpy as np

import auto_data_analysis as ada

# file_name = 'data/feature_0.csv'
# file_name = 'data/energydata_complete.csv'
# file_name = 'data/job.csv'
file_name = 'data/shanghai-ranking_2023.csv'
feature_data = pd.read_csv(file_name)

da = ada.DataAnalysis(feature_data)

da.visual_distribution(filter_view=False)
