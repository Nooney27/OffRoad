import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file_path = 'OffRoad\heightmap1.csv'
data = pd.read_csv(file_path)
print(data.head())

# smooth transition using a sinusoidal function
def smooth_transition(start, end, peak):
    length = end - start
    return peak * np.sin(np.linspace(0, np.pi, length))


data.loc[25:100, '0'] = smooth_transition(25, 101, 4)
data.loc[200:300, '0'] = smooth_transition(200, 301, 2)

# data.loc[20:105, '0'], data.loc[195:305, '0']
data.to_csv('OffRoad\heightmap_with_z_2.csv', index=False)


