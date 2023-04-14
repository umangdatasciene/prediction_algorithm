import pandas as pd

df = pd.read_csv("sales.csv")

df.isnull().sum()
import matplotlib.pyplot as plt

plt.figure(figsize=(15,8))

plt.plot(df.Month, df.Sales_Value)
plt.show()

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plt.rcParams.update({'figure.figsize':(9,7), 'figure.dpi':120})


fig, axes = plt.subplots(2, 2, sharex=True)
axes[0, 0].plot(df.Sales_Value); axes[0, 0].set_title('Original Series')
plot_acf(df.Sales_Value, ax=axes[0, 1])

axes[1, 0].plot(df.Sales_Value.diff()); axes[1, 0].set_title('1st Order Differencing')
plot_acf(df.Sales_Value.diff().dropna(), ax=axes[1, 1])
plt.show()
plt.show()

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plt.rcParams.update({'figure.figsize':(9,3), 'figure.dpi':120})

fig, axes = plt.subplots(1, 2, sharex=True)

axes[0].plot(df.Sales_Value.diff()); axes[0].set_title('1st Differencing')
axes[1].set(ylim=(0,5))

plot_pacf(df.Sales_Value.diff().dropna(), ax=axes[1])
plt.show()

from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_predict
import statsmodels


model = ARIMA(df.Sales_Value, order=(1,1,1))


model_fit = model.fit()


plot_predict(model_fit)
plt.show()