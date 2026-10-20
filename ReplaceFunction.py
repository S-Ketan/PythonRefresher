import numpy as np
import pandas as pd

df = pd.read_csv("weather_data(ReplaceFunction).csv")

# print(df.replace(-99999,np.nan))
print(
    df.replace(
        {
            "temperature": {-99999: np.nan, 28: 29},
            "windspeed": {-99999: np.nan},
            "event": {'0': "no event"},
        }
    )
)
