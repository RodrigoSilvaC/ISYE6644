import pandas as pd
import numpy as np
%matplotlib inline
from statsmodels.tsa.filters.hp_filter import hpfilter

df = pd.read_csv('forecast3.csv', index_col = 0, parse_dates = True)
df.asfreq('D').index
#Create dummy variable 'weekend'
df['weekend'] = np.where((df['day_of_week'] == 'Friday')|(df['day_of_week'] == 'Saturday')|(df['day_of_week'] == 'Sunday'),1,0)

def seasonal_mean(ts, n, lr=0.7):
    """
    Compute the mean of corresponding seasonal periods
    ts: 1D array-like of the time series
    n: Seasonal window length of the time series
    """
    out = np.copy(ts)
    for i, val in enumerate(ts):
        if np.isnan(val):
            ts_seas = ts[i-1::-n]  # previous seasons only
            if np.isnan(np.nanmean(ts_seas)):
                ts_seas = np.concatenate([ts[i-1::-n], ts[i::n]])  # previous and forward
            out[i] = np.nanmean(ts_seas) * lr
    return out
df['total_visitors'] = seasonal_mean(df['total_visitors'], n=7, lr=0.8)

df['total_visitors'].plot(figsize = (10,8))
ax = df['total_visitors'].plot(figsize = (16,5))

for day in df.query('holiday_flg ==1').index:
    ax.axvline(x = day, color = 'black', alpha = 0.5);

ax = df['total_visitors'].plot(figsize = (16,5))

for day in df.query('weekend ==1').index:
    ax.axvline(x = day, color = 'black', alpha = 0.5);

#Decompose plot
from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(df['total_visitors'])
result.plot();

#Split data between test and train
train_data = df.iloc[:round(len(df)*0.85)]
test_data = df.iloc[round(len(df)*0.85):]

#Calculate auto_arima
from pmdarima import auto_arima
auto_arima(df['total_visitors'],
          seasonal = True,
          m = 7).summary()

#Fit model
from statsmodels.tsa.statespace.sarimax import SARIMAX
model = SARIMAX(train_data['total_visitors'],
               order = (0,1,2),
               seasonal_order = (1,0,2,7),
               enforce_invertibility = False)

results = model.fit()
results.summary()

start = len(train_data)
end = len(train_data) + len(test_data) - 1
predictions = results.predict(start, end).rename('SARIMA Model')

# Plot test set vs predictions
ax = test_data['total_visitors'].plot(legend=True, figsize=(15, 8))
predictions.plot()

for day in df.query('weekend ==1').index:
    ax.axvline(x=day, color='black', alpha=0.5);

for day in df.query('holiday_flg ==1').index:
    ax.axvline(x=day, color='red', alpha=0.5);

fcast = results.predict(len(df), len(df) + 180, typ = 'levels').rename('SARIMAX Forecast')
df['total_visitors'].plot(legend = True)
fcast.plot(legend = True)