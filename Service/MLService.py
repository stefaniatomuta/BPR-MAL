import pickle
import pandas as pd
from Service.DataPreprocessingService import *
from Service.TransformService import *

model_pkl_path = "../Jupyter/technical_debt_model.pkl"
pca_pkl_path = "../Jupyter/pca.pkl"

def load_model(path):
    with open(path, 'rb') as file:
        model = pickle.load(file)
        return model

model = load_model(model_pkl_path)
pcas = load_model(pca_pkl_path)

# maybe some processing of the data here if needed in the future after the model is trained
def predict(data):
    transformed_data = transform_data(data)
    # print(transformed_data)
    return model.predict(transformed_data)


def transform_data(data):
    data = process_code_similarity(data)
    dataframe = pd.DataFrame.from_dict([data])
    # print(dataframe)
    columns = ['CodeSimilarity', 'ClassCouplingListing', 'CodeLinesPerFile', 'CommentLinesPerFile', 'ExternalAPICalls']
    dataframe = handle_list_to_median_system(columns, dataframe)
    dataframe.drop(
        columns=['Project_ID', 'Project_Name', 'ClassCouplingListing', 'CodeSimilarity', 'ExternalAPICalls',
                 'CodeLinesPerFile', 'CommentLinesPerFile'], axis=1, inplace=True)
    columns = dataframe.select_dtypes(include=np.number).columns
    dataframe = remove_outliers(columns, dataframe)
    imputed_nans = impute_nans(dataframe)
    imputed_nans.drop('ExternalAPICalls_Median', inplace=True, axis=1)
    dataframe = impute_zero_values(imputed_nans)
    # print(dataframe)
    dataframe = combine_term_frequency(dataframe)
    columns = ['CodeLines', 'CommentLines', 'MethodNumber',
               'ClassNumber', 'InterfaceNumber', 'InheritanceDeclarations',
               'UsingsNumber', 'HttpClientCalls', 'CSFiles', 'TermFrequency', 'CodeSimilarity_Median',
               'ClassCouplingListing_Median', 'CodeLinesPerFile_Median', 'CommentLinesPerFile_Median', 'TermFrequency',
               'EndOfLifeFramework']
    sqrt_columns(columns, dataframe)
    # print(dataframe)
    knn_df = knn_smoothing(dataframe,1)
    # print(knn_df)
    pca = pcas.transform(knn_df)
    # df = np.array([knn_df[0,1],knn_df[0,4]])
    return pca