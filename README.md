# 🏠 House Price Prediction API

A simple machine learning API to predict house prices using a regression model trained on the Kaggle House Prices dataset.  
This project includes both a FastAPI backend (for REST API) and an optional Streamlit frontend (for user interface).

---

## 🚀 Features

- 📈 Predict house prices based on input features
- 🧠 Machine learning model trained with scikit-learn
- ⚡ FastAPI for RESTful predictions
- 🖥️ Streamlit app for interactive use
- ☁️ Ready to deploy on Railway (or similar platforms)

---

## 🧰 Tech Stack

- Python 3.10+
- FastAPI + Uvicorn
- Pandas, NumPy
- Scikit-learn
- Joblib
- Streamlit (optional UI)

---

## 📁 Project Structure
```bash
house-price-prediction/

├── api.py # FastAPI REST API

├── app.py # Streamlit UI (optional)

├── train_model.py # Script to train and save model

├── house_price_model.pkl # Saved ML model

├── train.csv # Dataset used for training

├── requirements.txt # Python dependencies

├── Procfile # Deployment command for Railway

└── README.md # Project documentation
 ```
---

## 🎯 Input Features

```yaml
| Feature        | Type   | Description                             |
|----------------|--------|-----------------------------------------|
| `GrLivArea`    | float  | Ground living area (in square feet)     |
| `BedroomAbvGr` | int    | Number of bedrooms above ground         |
| `FullBath`     | int    | Number of full bathrooms                |
| `GarageCars`   | int    | Garage capacity (in number of cars)     |
| `YearBuilt`    | int    | Year the house was built                |
```
---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/gurusingagerry03/house-price-prediction.git
cd house-price-prediction
 ```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
 ```

### 3. Train the Model (Optional if house_price_model.pkl already exists)

```bash
python train_model.py
 ```

## 🧪 Running the API Locally

```bash
uvicorn api:app --reload
 ```
### Visit Swagger UI to test:

http://127.0.0.1:8000/docs

## 🖥️ Streamlit App (Optional)

### To launch the frontend UI:

```bash
streamlit run app.py
 ```
You can input values and get predicted prices in real-time.

## 🛰️ Deployment (Railway)

To deploy this API online using Railway:

1. Push this project to GitHub

2. Go to https://railway.app

3. Create a new project → Deploy from GitHub Repo

4. Railway will:

    - Auto-install requirements.txt

    - Run the API using Procfile

### 📄 Procfile Content:

```less
web: uvicorn api:app --host=0.0.0.0 --port=8000
 ```
Your deployed app will be available at:

https://your-project-name.up.railway.app

## 🛰️ 📚 Dataset Source

Kaggle: House Prices - Advanced Regression Techniques

## 👤 Author

Built by Gerry0303

GitHub: @gurusingagerry03
