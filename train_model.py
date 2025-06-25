import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import joblib

# Load dataset
df = pd.read_csv("train.csv")

# Select important features
X = df[["GrLivArea", "BedroomAbvGr", "FullBath", "GarageCars", "YearBuilt"]]
y = df["SalePrice"]

# Clean missing values
X = X.dropna()
y = y[X.index]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Calculate RMSE
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# Save model and RMSE
joblib.dump({"model": model, "rmse": rmse}, "house_price_model.pkl")
print(f"✅ Model saved as house_price_model.pkl with RMSE: {rmse:.2f}")
