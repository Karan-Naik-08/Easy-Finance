install.packages("forecast")

library(forecast)
data <- read.csv('Inflation Data - Sheet1.csv')
png(file = "TimeSeriesGFG.png")
plot(BJsales,main = "Graph without forecasting", col.main ="darkgreen")
dev.off()
png(file= "TimeSeriesARIMAGFG.png")

fit <- auto.arima(data)
forecastedValues <- forecast(fit, 3)
print(forecastedValues)
print(BJsales)
