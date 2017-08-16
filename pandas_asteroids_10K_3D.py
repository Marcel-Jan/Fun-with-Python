import pandas as pd
import matplotlib.pyplot as plt
import pickle
import ijson
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import style
style.use("seaborn-paper")


asteroid_df = pd.read_pickle('asteroids10K_aei.pickle')

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

