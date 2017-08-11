import pandas as pd
import matplotlib.pyplot as plt
import pickle
import numpy as np
import ijson
from sklearn.cluster import MeanShift


filename = "D:\\Stuur\\mpcorb_10kasteroids.json"
# filename = "D:\\Stuur\\mpcorb_extended_20170810.json"

asteroid_data = []

with open(filename, 'r') as f:
    objects = ijson.items(f, 'item')
    for row in objects:
    	selected_row = dict()
    	selected_row = {"a": row["a"], "e": row["e"], "i": row["i"]}
    	asteroid_data.append(selected_row)

asteroid_df = pd.DataFrame.from_dict(asteroid_data)
print(asteroid_df.describe())

# pickle_out = open('asteroids_aei_20170810.pickle', 'wb')
# pickle.dump(asteroid_df, pickle_out)
# pickle_out.close()

# asteroid_df = pd.read_pickle('asteroids_aei_20170810.pickle')

# plt.scatter(asteroid_df.a, asteroid_df.i, label='scatter', color='k', marker='.', s=1)

asteroid_df.drop(['i'], 1, inplace=True)

ms = MeanShift()
ms.fit(asteroid_df)
labels = ms.labels_
cluster_centers = ms.cluster_centers_

print(cluster_centers)
n_clusters_ = len(np.unique(labels))
print("Number of estimated clusters:", n_clusters_)

colors = 10*['r','g','b','c','k','y','m']

for i in range(len(asteroid_df)):
    plt.scatter(asteroid_df.a, asteroid_df.e, label='asteroid data', c=colors[labels[i]], marker='.', s=1)

# ax.scatter(cluster_centers[:,0],cluster_centers[:,1],
#             marker="x",color='b', s=150, linewidths = 5, zorder=10)

plt.scatter(cluster_centers[:,0], cluster_centers[:,1], label='centroids', color='b', marker='x', s=150, linewidths = 5, zorder=10)

# plt.xlim(2, 3.5)
# plt.ylim(0, .5)

plt.xlabel('Semimajor axis')
plt.ylabel('Eccentricity')

plt.title('All known asteroids')
# plt.legend()
plt.show()
