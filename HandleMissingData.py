import pandas as pd
df=pd.read_csv('weather_data(HandleMissingData).csv', parse_dates=["day"])
df.set_index("day", inplace=True)
# print(df)

# new_df=df.fillna({
#     'temperature':0,
#     'windspeed':0,
#     'event': 'no event'
#     })
# new_df= df.ffill() #Take previous row value
# new_df= df.bfill() #Take next row value
# new_df=df.dropna() #removes the rows with missing values
new_df=df.copy() # created copy of main dataframes
# new_df[new_df.select_dtypes(include='number').columns]=new_df[new_df.select_dtypes(include='number').columns].interpolate() #Only columns with Numeric value would be interpolated and method='linear' is default
new_df['event']=new_df['event'].ffill() # Using ffill() for string datatype
new_df[new_df.select_dtypes(include='number').columns]=new_df[new_df.select_dtypes(include='number').columns].interpolate(method='time') # observation between dates

print(new_df)
