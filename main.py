from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd
import pickle

app = FastAPI()

with open( 'rf_model.pkl', 'rb' ) as file :
    
    model = pickle.load( file )

class LoanInput(BaseModel):
    no_of_dependents: int
    education: str
    self_employed:str
    income_annum: int
    loan_amount: int
    loan_term: int
    cibil_score: int
    residential_assets_value: int
    commercial_assets_value: int
    luxury_assets_value: int
    bank_asset_value: int
     
    

@app.post("/predict")
def predict(input_data: LoanInput):
    try:
        data = pd.DataFrame([{
    "no_of_dependents": input_data.no_of_dependents,
    "education": input_data.education,
    "self_employed": input_data.self_employed,
    "income_annum": input_data.income_annum,
    "loan_amount": input_data.loan_amount,
    "loan_term": input_data.loan_term,
    "cibil_score": input_data.cibil_score,
    "residential_assets_value": input_data.residential_assets_value,
    "commercial_assets_value": input_data.commercial_assets_value,
    "luxury_assets_value": input_data.luxury_assets_value,
    "bank_asset_value": input_data.bank_asset_value
}])
        

   
        
        
        prediction = model.predict(data)[0]
        print(  prediction)
        if prediction==0:
            return 'Approved'
        else :
            return 'Rejected'
        
    except Exception as e:
        return {"error": str(e)}
  