from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import os
import uvicorn,pandas
from fastapi import FastAPI
from pydantic import BaseModel

class Banknote(BaseModel):
    variance: float   # variance of features
    skewness: float   # skewness of features
    curtosis: float   # curtosis of features
    entropy: float    # entropy of features

app=FastAPI()
model_path = "model.pkl"


with open(model_path, "rb") as file:
    model = pickle.load(file)

@app.get('/welcome')
def index(messege:str):
    return f"Hello {messege}"

@app.post('/predict')
def prdict(data:Banknote):
    #print('Hello')
    v=data.variance
    s=data.skewness
    c=data.curtosis
    e=data.entropy
    features = np.array([[v, s, c, e]])
    predict=model.predict(features)
    print(predict)
    if predict[0]>.5:
        predict='Fake'
    else:
        predict="Okay"
    return {'predict':predict}
    

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)