import pandas as pd
# df=pd.read_csv('/home/ketan/Desktop/UNI/AIML/weather_data.csv')
# print(df)
weatherData={
    'day':[1/1/2017,1/2/2017,1/3/2017,1/4/2017,1/5/2017,1/6/2017],
    'temperature':[32,35,38,24,32,31],
    'windspeed':[6,7,4,7,2,2],
    'event':['rain', 'sunny','snow', 'snow', 'rain', 'sunny'],
}

df=pd.DataFrame(weatherData)
print(df.head(2)) #Top 2 rows
print(df.tail(1)) # bottom 1 row
print("Events: ",df.event)
print("Columns: ",df.columns)
print("Shape: ",df.shape)
print(df[['event','temperature','windspeed']][2:5]) #Slicing
print(df.temperature.max())
print(df.temperature.mean())
print(df.temperature.min())
print(df.temperature.std()) # standard deviation
print(df.describe()) #Describe Max, min, ount etc for the columns
print(df[['temperature','windspeed']][df.temperature==df.temperature.max()])
