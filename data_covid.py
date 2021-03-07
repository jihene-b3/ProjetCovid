import pandas as pd
import numpy as np
from scipy.stats.stats import pearsonr  
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
from datetime import datetime
from sklearn.model_selection import train_test_split
import math
import matplotlib.pyplot as plt
from download import download 


url1 ='https://www.data.gouv.fr/fr/datasets/r/0b66ca39-1623-4d9c-83ad-5434b7f9e2a4'
path_target = "./covid.csv"
download(url1, path_target, replace=True)
df_covid = pd.read_csv("covid.csv")
df_covid.head(n=100)
path_target = "./covid.csv"
download(url1, path_target, replace=True)
df_covid = pd.read_csv("covid.csv")
df_covid.head(n=100)