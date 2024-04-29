# plot Track
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### 2D Plot ###

file_path = 'OffRoad\heightmap_with_z.csv'
data = pd.read_csv(file_path, delimiter=';', skiprows=3)
column_names = ['s_m', 'x_m', 'y_m', 'psi_rad', 'kappa_radpm', 'vx_mps', 'unknown', 'z_m']
data.columns = column_names

# Remove any trailing commas from the 'z_m' column and convert to float
data['z_m'] = data['z_m'].str.replace(',', '').astype(float)
# Check for any NaN values and handle them
data['z_m'].fillna(0, inplace=True)


fig, ax = plt.subplots()
scatter = ax.scatter(data['x_m'], data['y_m'], c=data['z_m'], cmap='viridis')
colorbar = fig.colorbar(scatter)
colorbar.set_label('Height (z_m)')
ax.set_xlabel('X Coordinate (x_m)')
ax.set_ylabel('Y Coordinate (y_m)')
ax.set_title('Race Track with Height Gradient')

plt.show()

### 3D Plot ###
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data['x_m'], data['y_m'], data['z_m'])
ax.set_xlabel('X Coordinate (x_m)')
ax.set_ylabel('Y Coordinate (y_m)')
ax.set_zlabel('Height (z_m)')
ax.set_title('3D Plot of Track Data')

# Rescale z axis
ax.set_zlim(0, 20)
plt.show()