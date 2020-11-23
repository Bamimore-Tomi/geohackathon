from typing import Dict,Optional

from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def index():
    return '<h2>Welcome to this api, go to /api/docs to see documentation</h2>'

@app.get('/api')
def predict(q1: Optional[float]=None , q2 : Optional[float]=None , q3: Optional[float]=None ) -> Dict:
    return {"Q1":q1, "Q2":q2, "Q3":q3}
