import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

ticker = "TSLA"
print(f"Fetching data for {ticker}...")
data = yf.download(ticker, start="2025-01-01", end="2026-06-01")

data['Next_Close'] = data['Close'].shift(-1)
data = data.dropna()

X = data[['Open', 'High', 'Low', 'Volume']]
y = data['Next_Close']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"\nModel Evaluation:")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R2 Score: {r2:.4f}")

plt.figure(figsize=(12, 6))
plt.plot(y_test.index, y_test.values, label="Actual Next Close", color="blue", linewidth=1.5)
plt.plot(y_test.index, y_pred, label="Predicted Next Close", color="red", linestyle="--", linewidth=1.5)

plt.title(f"{ticker} Stock Price Prediction - Actual vs Predicted (Short-Term)")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.show()
