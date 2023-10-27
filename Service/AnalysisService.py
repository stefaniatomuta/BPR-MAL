import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as stats
from Constants.variables import DATA_PATH

def read_data():
    df = pd.read_csv(DATA_PATH)
    print(df.info())
    print(df.head())

read_data()



