from typing import Dict,Optional
import numpy as np
import pickle
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
model = pickle.load(open('model.pkl','rb'))

class Prediction(BaseModel):
    prediction: int

@app.get('/')
def index():
    return '<h2>Welcome to this api, go to /docs to see documentation</h2>'

@app.get('/api/', response_model=Prediction)
def predict(q1: Optional[float]=None , q2 : Optional[float]=None , q3: Optional[float]=None):
    df_test = np.array([q1,q2,q3])
    df_test = df_test.reshape(1,-1)
    prediction = model.predict(df_test)
    response = {"prediction":prediction[0]}
    return response
