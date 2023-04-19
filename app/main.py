from fastapi import Body, FastAPI
import numpy as np
import pandas as pd
from app.schema import Data
import pickle


with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

@app.post("/v1/predict/")
def predict_iris(data: Data):
    data_dict = data.dict()
    df = pd.DataFrame(data_dict['data'])
    prediction = model.predict(df)

    return {'predictions': prediction.tolist()}