from fastapi import FastAPI
from pydantic import BaseModel

import joblib
app=FastAPI()

model=joblib.load('model_trained.pkl')

class HOUSEInput(BaseModel):
     Avg_Area_Income:float
     Avg_Area_House_Age:float
     Avg_Area_Number_of_Rooms:float
     Avg_Area_Number_of_Bedrooms:float
     Area_Population:float

@app.get('/')
def home():
    return {"Message":"USA Housing Price Prediction API"} 

@app.post("/predict")
def Prediction(data:HOUSEInput):
    input_list=[[
       data.Avg_Area_Income,
       data.Avg_Area_House_Age,
       data.Avg_Area_Number_of_Rooms,
       data.Avg_Area_Number_of_Bedrooms,
       data.Area_Population
    ]]
    final_prediction=model.predict(input_list)


    
    return{
         "Predicted Price":float(final_predictionprediction[0])
     }

