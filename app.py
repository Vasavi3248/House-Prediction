import streamlit as st
import joblib

# Load the trained model
model = joblib.load("model_trained.pkl")

# Title
st.title("🏠 House Price Prediction")

st.write("House Price Prediction using Machine Learning")

# Input fields
Avg_Area_Income = st.number_input("Average Area Income", min_value=0.0)
Avg_Area_House_Age = st.number_input("Average Area House Age", min_value=0.0)
Avg_Area_Number_of_Rooms = st.number_input("Average Number of Rooms", min_value=0.0)
Avg_Area_Number_of_Bedrooms = st.number_input("Average Number of Bedrooms", min_value=0.0)
Area_Population = st.number_input("Area Population", min_value=0.0)

# Prediction button
if st.button("House Prediction"):

    input_list = [[
        Avg_Area_Income,
        Avg_Area_House_Age,
        Avg_Area_Number_of_Rooms,
        Avg_Area_Number_of_Bedrooms,
        Area_Population
    ]]

    # Predict
    final_prediction = model.predict(input_list)

    # Display result
    predicted_price = round(final_prediction[0], 2)

    st.success(f"🏠 Predicted House Price: ${predicted_price:,.2f}")
    


    