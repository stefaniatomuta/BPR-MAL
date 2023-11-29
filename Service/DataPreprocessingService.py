import numpy as np
import ast
from sklearn.neighbors import KNeighborsRegressor
from sklearn.impute import KNNImputer
from sklearn import preprocessing, decomposition
import pandas as pd
from scipy import stats

def global_boundaries(data):
    global_max = 0
    global_min = 9999

    for row in data:
        row_list = ast.literal_eval(row)
        row_number = [int(x) for x in row_list]
        if row_number:
            row_max = np.max(row_number)
            row_min = np.min(row_number)
            if row_max > global_max:
                global_max = row_max
            if row_min < global_min:
                global_min = row_min

    return global_max, global_min

def get_boundaries(lower, higher, numberOfBins):
    boundaries = np.linspace(lower, higher, numberOfBins)
    boundaries[-1] = np.inf
    return boundaries

def handle_column_data(column):
    return column.apply(lambda x: np.array([float(value) for value in x.strip('[]').split(',') if value]))

def handle_list_to_median(columns:list, df: pd.DataFrame) -> pd.DataFrame:
    '''
    Description:
        Processes the dataframe and creates new columns with the median value in each row of the column if it is a list
    Args:
        columns (list(string)): a list of column names that need to be processes. The data in these columns must be a list of numbers

        df (Pandas.Dataframe): the dataframe containing the columns in question
    Returns:
        Dataframe: a dataframe with new columns created for each column given in 'columns'.
        The value in the new column is the median value of each list in each row
    '''
    print(type(df))
    for column in columns:
        print(column)
        data = df[column].apply(lambda x: np.array([float(value) for value in x.strip('[]').split(',') if value]))
        data2 = data.apply(lambda x: np.median(x))
        df[f'{column}_Median'] = data2
    return df

def remove_outliers(columns, df):
    for column in columns:
        std = df[column].std()
        median = df[column].median()
        df.loc[np.abs(df[column] - median) > std, column] = np.nan
    return df

def impute_nans(df):
    imputer = KNNImputer(n_neighbors=2, weights="uniform")
    columns = df.columns
    return pd.DataFrame(imputer.fit_transform(df), columns=columns)
def impute_zero_values(df):
    imputer = KNNImputer(n_neighbors=2, weights="uniform",missing_values=0)
    columns = df.columns
    return pd.DataFrame(imputer.fit_transform(df), columns=columns)

def combine_term_frequency(df):
    term_frequency_columns = ['IfFrequency', 'ForFrequency', 'WhileFrequency', 'ForEachFrequency']
    df['TermFrequency'] = df[term_frequency_columns].sum(axis=1)
    return df.drop(columns=term_frequency_columns, axis=1)

def sqrt_columns(columns, df):
    for column in columns:
        df[column] = np.sqrt(df[column])


def yeojohnson(columns, df):
    for column in columns:
        df[column] = stats.yeojohnson(df[column])[0]


def knn_smoothing(data, window_size):
    X = np.arange(len(data)).reshape(-1, 1)
    knn = KNeighborsRegressor(n_neighbors=window_size)
    knn.fit(X, data)
    smoothed_data = knn.predict(X)
    return smoothed_data

def create_pca(df):
    X_s = preprocessing.StandardScaler().fit_transform(df)
    pcas = decomposition.PCA(n_components=2)
    return pcas.fit_transform(X_s)