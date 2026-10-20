import numpy as np
import pandas as pd

a=np.array([1,5,9])
b=np.array([[1,5],[2,6],[3,7]])
print(b.ndim)
print(b.shape)

# c=np.zeros((3,4))
c=np.ones((3,4))
print(c)

d=np.linspace(1,100,10)
print(d)
df=pd.read_csv("/home/ketan/Desktop/AIML/weather_data.csv")
df
