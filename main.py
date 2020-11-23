from typing import Dict,Optional

from fastapi import FastAPI
app = FastAPI()

@app.get('/api')
def index():
    return 'Welcome to this api, go to /api/docs to see documentation'

@app.get('/api')
def predict(q1: float , q2 : float , q3: float ) -> Dict:
    return {'you':q1}
