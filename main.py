from typing import Dict,Optional

from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def root(q1: float , q2 : float , q3: float ) -> Dict:
    return {'you':q1}