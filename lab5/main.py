import pandas as pd
import random 
import matplotlib.pyplot as plt

data1=pd.read_csv("Delhi_Climate.csv", parse_dates=True, index_col="date")

#TimeSeries
data_1 = pd.DataFrame({"Weight": [random.randint(1, 10) for i in range(10)],
                          "Time": pd.date_range('20181101', freq="D", periods=10)})
data_2 = pd.DataFrame({"Height": [random.randint(1, 10) for i in range(10)],
                          "Time": pd.date_range('20181101', freq="D", periods=10)}, )
data_1 = data_1.set_index("Time")
data_2 = data_2.set_index("Time")
data_all = pd.merge_asof(data_1, data_2, on="Time").set_index("Time")

print(data_all)

#task1
print(data1.plot(y='humidity'))
plt.show()
print(data1.loc['2013'].plot(y='humidity'))
plt.show()
print(data1.loc['2016-02'].plot(y='humidity'))
plt.show()
print(data1.loc['2014-01':'2016-3'].plot(y='humidity'))
plt.show()
print(data1.loc['2014-01':'2015-12'].plot(y='humidity'))
plt.show()

#task2
print(data1['wind_speed'].loc['2015-01':'2015-12'].astype('float').resample('Y').mean())
print(data1['wind_speed'].loc['2014-01':'2014-12'].astype('float').resample('M').mean())
print(data1['wind_speed'].loc['2016-Sep':'2016-Nov'].astype('float').resample('W').mean())
print(data1['wind_speed'].loc['2013-03':'2013-05'].astype('float').asfreq('D').pct_change().plot(y='wind_speed'))
plt.show()
print(data1['wind_speed'].loc['2015-02-01':'2015-02-28'].astype('float').rolling(4).mean().plot())
plt.show()