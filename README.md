# 🏠 House Price Prediction using Machine Learning

## 📌 Project Overview

The **House Price Prediction** project is a Machine Learning web application that estimates the selling price of a house based on various property features such as the number of bedrooms, bathrooms, living area, lot size, floors, waterfront, view, condition, and other housing attributes.

The application is developed using **Python**, **Streamlit**, and **Scikit-learn**. A **Linear Regression** (or your chosen algorithm) model is trained on historical housing data and deployed through an interactive web interface, allowing users to enter property details and receive an instant price prediction.

This project demonstrates the complete Machine Learning workflow, including data preprocessing, exploratory data analysis, model training, model evaluation, and deployment.

---

## 🚀 Features

- Predicts house prices based on user inputs.
- Interactive and responsive web interface built with Streamlit.
- Real-time price prediction.
- Data preprocessing and feature engineering.
- Machine Learning model trained using Scikit-learn.
- Simple and user-friendly interface.
- End-to-end Machine Learning deployment.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Pickle

---

## 📂 Project Structure

```
House_Prediction/
│
├── app.py
├── model.pkl
├── House_Price_Prediction.ipynb
├── house_data.csv
├── requirements.txt
├── README.md
│
├── static/
│
└── images/
```

---

## 📊 Dataset Information

The dataset contains information about different houses, including:

- Number of Bedrooms
- Number of Bathrooms
- Living Area
- Lot Area
- Number of Floors
- Waterfront
- View
- Condition
- Grade
- Above Ground Area
- Basement Area
- Year Built
- Year Renovated
- Zip Code
- Latitude
- Longitude
- Living Area (Nearest)
- Lot Area (Nearest)

**Target Variable**

- House Price

---

## ⚙️ Machine Learning Workflow

1. Load the housing dataset.
2. Perform data cleaning and preprocessing.
3. Handle missing values.
4. Encode categorical features (if required).
5. Split the dataset into training and testing sets.
6. Train the Machine Learning model.
7. Evaluate model performance.
8. Save the trained model using Pickle.
9. Develop a Streamlit web application.
10. Predict the house price based on user input.

---

## 📈 Machine Learning Model

- **Algorithm:** Linear Regression *(or Random Forest Regression, Decision Tree Regression, XGBoost, etc.)*
- **Problem Type:** Regression
- **Library:** Scikit-learn

---

## ▶️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/House_Prediction.git
```

### Navigate to the project directory

```bash
cd House_Prediction
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install the required packages

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## 📊 Model Evaluation

The model performance can be evaluated using regression metrics such as:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## 💻 Application Screenshots

### Home Page

Add a screenshot of the application's home page here.

```text
![alt text](<house prediction home page.png>)
```

### Prediction Result

Add a screenshot of the prediction result page here.

```text
![alt text](<house prediction result page.png>)
```

---

## 🌟 Future Enhancements

- Deploy the application on Streamlit Community Cloud.
- Improve prediction accuracy using advanced algorithms.
- Add interactive data visualizations.
- Implement feature importance analysis.
- Allow batch predictions using CSV upload.
- Integrate location-based house price estimation.
- Optimize hyperparameters for better performance.

---

## 📚 Learning Outcomes

This project helped me gain practical experience in:

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Regression Algorithms
- Model Evaluation
- Feature Engineering
- Streamlit Web Development
- Machine Learning Model Deployment
- End-to-End Data Science Workflow

---

## 👩‍💻 Author

**Vasavi Maradugu**

GitHub: https://github.com/your-github-username

LinkedIn: https://linkedin.com/in/your-linkedin-profile

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

