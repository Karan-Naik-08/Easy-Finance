# Read the CSV file
data <- read.csv('Inflation.csv')

# Create a time series object
inflation_ts <- ts(data$India, start = 1960, end = 2022, frequency = 1)

# Load the forecast library
library(forecast)

# Fit an ARIMA model to the time series
model <- auto.arima(inflation_ts)

# Forecast future values
forecast_values <- forecast(model, h = 3)

# Print the forecast
print(forecast_values)

# Plot the forecast
plot(forecast_values)
