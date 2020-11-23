from typing import Dict,Optional

from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def index():
    return '<h2>Welcome to this api, go to /api/docs to see documentation</h2>'

@app.get('/api')
def predict(q1: float , q2 : float , q3: float ) -> Dict:
    return {'you':q1}
