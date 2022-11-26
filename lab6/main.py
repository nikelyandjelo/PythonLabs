import pandas as pd

data=pd.DataFrame(pd.read_html('Version 6.html',index_col="date")[0])

data.rename(columns={'date':'дата','meantemp': 'середня температура','humidity': 'волoгість', 'wind_speed': 'швидкість вітра', 'meanpressure': 'середній тиск'}, inplace=True)
data=data.drop("Unnamed: 0",axis=1)
data=data.dropna()
data['волoгість']=data['волoгість'].astype('int')
data=data.drop_duplicates('волoгість')
humidity=data['волoгість'].loc["2014-01-01" : "2016-01-01"]
humidity1=data['волoгість'].loc["2013-01-01" : "2013-12-12"]
humidity2=pd.concat([humidity,humidity1])
humidity2.sort_values(inplace=True)
print(humidity2)