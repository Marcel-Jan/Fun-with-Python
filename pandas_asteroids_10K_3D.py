import pandas as pd
import matplotlib.pyplot as plt
import pickle
import numpy as np
import ijson
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import style
style.use("ggplot")

filename = "D:\\Stuur\\mpcorb_10kasteroids.json"
# filename = "D:\\Stuur\\mpcorb_extended.json"

columns_i_want = ["a", "e", "i"]
asteroid_data = []

with open(filename, 'r') as f:
    objects = ijson.items(f, 'item')
    for row in objects:
    	selected_row = dict()
    	selected_row = {"a": float(row["a"]), "e": float(row["e"]), "i": float(row["i"])}
    	asteroid_data.append(selected_row)

# print(asteroid_data)
asteroid_df = pd.DataFrame.from_dict(asteroid_data)
# print(asteroid_df)
print(asteroid_df.describe())

# pickle_out = open('asteroids_aei.pickle', 'wb')
# pickle.dump(asteroid_df, pickle_out)
# pickle_out.close()

# asteroid_df = pd.read_pickle('asteroids_aei.pickle')
# print(asteroid_df.a.describe())
# print(asteroid_df.e.describe())


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(asteroid_df.a, asteroid_df.i, asteroid_df.e, color='k', marker='.')

ax.set_xlim(2, 3.5)
ax.set_ylim(0, 20)
ax.set_zlim(0, 0.5)

ax.set_xlabel('Semimajor axis')
ax.set_ylabel('Inclination')
ax.set_zlabel('Eccentricity')
ax.set_title('First 10,000 asteroids discovered')

plt.show()

