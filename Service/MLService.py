import pickle
model_pkl_path = "Jupyter/technical_debt_model.pkl"

def load_model(path):
    with open(path, 'rb') as file:
        model = pickle.load(file)
        return model

model = load_model(model_pkl_path)

# maybe some processing of the data here if needed in the future after the model is trained
def predict(data):
    return model.predict(data)
