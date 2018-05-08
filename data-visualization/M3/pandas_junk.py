from matplotlib import pyplot as plt
import pandas as pd

data = {
    'year': [2008, 2012, 2016],
    'attendees': [112, 231, 729],
    'average age': [24, 41, 31]
}

df = pd.DataFrame(data)
print(df)