from pathlib import Path
import pandas as pd
import tarfile
import urllib.request
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as stats
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

def read_data():
    df = pd.read_csv('data.csv')
    print(df.info())


