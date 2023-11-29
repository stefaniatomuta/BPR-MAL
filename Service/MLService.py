import pickle
import pandas as pd
from DataPreprocessingService import *

model_pkl_path = "Jupyter/technical_debt_model.pkl"

def load_model(path):
    with open(path, 'rb') as file:
        model = pickle.load(file)
        return model

model = load_model(model_pkl_path)

# maybe some processing of the data here if needed in the future after the model is trained
def predict(data):
    transformed_data = transform_data(data)
    return model.predict(transformed_data)


def transform_data(data):
    dataframe = pd.DataFrame(data)
    columns = ['CodeSimilarity', 'ClassCouplingListing', 'CodeLinesPerFile', 'CommentLinesPerFile', 'ExternalAPICalls']
    dataframe = handle_list_to_median(columns, dataframe)
    dataframe.drop(
        columns=['Project_ID', 'ClassCouplingListing', 'CodeSimilarity', 'ExternalAPICalls', 'ExternalAPIExtracted',
                 'CodeLinesPerFile', 'CommentLinesPerFile'], axis=1, inplace=True)
    columns = dataframe.select_dtypes(include=np.number).columns
    dataframe = remove_outliers(columns,dataframe)
    imputed_nans = impute_nans(dataframe)
    imputed_nans.drop('ExternalAPICalls_Median', inplace=True, axis=1)
    dataframe = impute_zero_values(imputed_nans)
    dataframe = combine_term_frequency(dataframe)
    columns = ['CodeLines', 'CommentLines', 'MethodNumber',
               'ClassNumber', 'InterfaceNumber', 'InheritanceDeclarations',
               'UsingsNumber', 'HttpClientCalls', 'CSFiles', 'TermFrequency', 'CodeSimilarity_Median',
               'ClassCouplingListing_Median', 'CodeLinesPerFile_Median', 'CommentLinesPerFile_Median', 'TermFrequency',
               'EndOfLifeFramework']
    yeojohnson(columns, dataframe)
    knn_df = knn_smoothing(dataframe,5)
    pca = create_pca(knn_df)
    return pca