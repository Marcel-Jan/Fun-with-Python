import pandas as pd
import matplotlib.pyplot as plt

asteroid_df = pd.read_json('D:\\Stuur\\mpcorb_10kasteroids.json')
plt.scatter(asteroid_df.a, asteroid_df.e, color='k', marker='.', s=1)
plt.xlim(2, 3.5)
plt.ylim(0, .8)
plt.xlabel('Semimajor axis (AU)')
plt.ylabel('Eccentricity')
plt.title('First 10K asteroids discovered')
plt.show()
