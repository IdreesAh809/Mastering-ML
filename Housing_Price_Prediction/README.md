# 📌 Housing Price Prediction
A **machine learning project** that predicts house prices based on various features using **XGBoost, Linear Regression, and other models**.
## 📂 Project Structure
Housing_Price_Prediction/ ├── data/ # Contains datasets │ ├── raw/ # Original dataset │ ├── processed/ # Cleaned & feature-engineered dataset ├── notebooks/ # Jupyter Notebooks │
├── 01_data_exploration.ipynb │ ├── 02_data_preprocessing.ipynb │ ├── 03_feature_engineering.ipynb │ ├── 04_model_training.ipynb ├── models/ # Trained models │ ├── best_model.pkl # Saved XGBoost model
├── README.md # Project Overview ├── requirements.txt # Dependencies ├── .gitignore # Ignore unnecessary files

## 📊 Dataset
- **Source:** [California Housing Prices Dataset](https://www.kaggle.com/datasets/camnugent/california-housing-prices)
- **Description:** Includes features such as location, number of rooms, area, and price.
- **Preprocessing:** Missing values handled, categorical encoding, and feature scaling applied.
  
## ⚡ Installation
### 1️⃣ Clone the Repository
git clone https://github.com/IDREESAh809/Housing_Price_Prediction.git
cd Housing_Price_Prediction

### 2️⃣ Install Dependencies
pip install -r requirements.txt

 ### 3️⃣ Models Used & Accuracy
Model	R² Score	RMSE
Linear Regression	0.62	67,000
Decision Tree	0.75	52,000
XGBoost	0.82	46,100 ✅

### 4️⃣
Final Model Deployment
import joblib
model = joblib.load("models/best_model.pkl")


