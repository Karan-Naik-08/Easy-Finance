import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('Models/Inflation rate/Inflation.csv')

# Create a time series object
inflation_series = pd.Series(data['India'].values, index=pd.date_range(start='1960', end='2022', freq='AS'))

# Fit an ARIMA model to the time series
model = sm.tsa.ARIMA(inflation_series, order=(1, 1, 1))
results = model.fit()

# Forecast future values
forecast_values = results.forecast(steps=3)

# Print the forecast
print(forecast_values)

# Plot the forecast
plt.plot(inflation_series, label='Observed')
plt.plot(pd.date_range(start='2023', periods=3, freq='AS'), forecast_values, label='Forecast')
plt.legend()
plt.show()
