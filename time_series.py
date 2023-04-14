import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('time_series_data.csv', parse_dates=['date'], index_col='date')

# Plot the time series
plt.plot(data)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Time Series Data')
plt.show()

# Compute rolling mean and standard deviation
rolling_mean = data.rolling(window=2).mean()
rolling_std = data.rolling(window=2).std()
print ("rolling_mean")

# Plot the rolling statistics
plt.plot(data, label='Original')
plt.plot(rolling_mean, label='Rolling Mean')
plt.plot(rolling_std, label='Rolling Std')
plt.legend()
plt.title('Rolling Mean and Standard Deviation')
plt.show()

# Perform Dickey-Fuller test for stationarity
from statsmodels.tsa.stattools import adfuller

result = adfuller(data['value'])
print('ADF Statistic:', result[0])
print('p-value:', result[1])
print('Critical Values:', result[4])