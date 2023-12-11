import pickle
from Service.MAL.DataPreprocessingService import *
from Service.ETL.TransformService import *

model_pkl_path = "./Jupyter/technical_debt_model.pkl"
pca_pkl_path = "./Jupyter/pca.pkl"

def load_model(path):
    with open(path, 'rb') as file:
        model = pickle.load(file)
        return model

model = load_model(model_pkl_path)
pcas = load_model(pca_pkl_path)


manual_labels = {0:"Medium", 1:"High", 2:"Highest", 3:"Low"}
def map_manual_labels(cluster_label):
    return manual_labels[cluster_label]

def predict(data):
    transformed_data = transform_data(data)
    return map_manual_labels(model.predict(transformed_data)[0])

def transform_data(data):
    data = transform_extracted_data(data)
    dataframe = pd.DataFrame.from_dict([data])
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
    dataframe = combine_term_frequency(dataframe)
    columns = ['CodeLines', 'CommentLines', 'MethodNumber',
               'ClassNumber', 'InterfaceNumber', 'InheritanceDeclarations',
               'UsingsNumber', 'HttpClientCalls', 'CSFiles', 'TermFrequency', 'CodeSimilarity_Median',
               'ClassCouplingListing_Median', 'CodeLinesPerFile_Median', 'CommentLinesPerFile_Median', 'TermFrequency',
               'EndOfLifeFramework']
    sqrt_columns(columns, dataframe)
    columns = ['CodeLines', 'CommentLines', 'MethodNumber',
       'ClassNumber', 'InterfaceNumber','InheritanceDeclarations', 
       'UsingsNumber','HttpClientCalls', 'CSFiles','TermFrequency','CommentLinesPerFile_Median', 'TermFrequency']
    sqrt_columns(columns, dataframe)
    knn_df = knn_smoothing(dataframe, 1)
    pca = pcas.transform(knn_df)
    return pca


