import pandas as pd
import matplotlib.pyplot as plt
import pickle
import ijson

filename = "D:\\Stuur\\mpcorb_extended_20170810.json"

asteroid_data = []

with open(filename, 'r') as f:
    objects = ijson.items(f, 'item')
    for row in objects:
    	selected_row = dict()
    	selected_row = {"a": float(row["a"]), "e": float(row["e"]), "i": float(row["i"])}
    	asteroid_data.append(selected_row)

asteroid_df = pd.DataFrame.from_dict(asteroid_data)
print(asteroid_df.describe())

pickle_out = open('asteroids_aei_20170816.pickle', 'wb')
pickle.dump(asteroid_df, pickle_out)
pickle_out.close()

asteroid_df = pd.read_pickle('asteroids_aei_20170816.pickle')


plt.scatter(asteroid_df.a, asteroid_df.e, label='scatter', color='k', marker='.', s=1)

plt.xlim(2, 3.5)
plt.ylim(0, .5)

plt.xlabel('Semimajor axis')
plt.ylabel('Eccentricity')

plt.title('All known asteroids')
plt.show()
