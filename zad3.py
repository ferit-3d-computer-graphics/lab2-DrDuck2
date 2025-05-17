import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.animation import FuncAnimation

num_points = 500
n_clusters = 10

points = np.random.rand(num_points, 3) * 10  

kmeans = KMeans(n_clusters=n_clusters, n_init=10)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

scat = ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='gray', s=10, alpha=0.6)
centers = np.zeros((n_clusters, 3))
centers_scat = ax.scatter(centers[:, 0], centers[:, 1], centers[:, 2], c='red', s=100, marker='X')

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Dynamic Point Cloud with Real-Time KMeans Clustering')

def update(frame):
    global points

    motion = (np.random.rand(num_points, 3) - 0.5) * 0.2
    points += motion
    points = np.clip(points, 0, 10)  

    kmeans.fit(points)
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_

    scat._offsets3d = (points[:, 0], points[:, 1], points[:, 2])
    scat.set_array(labels)

    centers_scat._offsets3d = (centers[:, 0], centers[:, 1], centers[:, 2])

    return scat, centers_scat

ani = FuncAnimation(fig, update, frames=200, interval=100, blit=False)
plt.show()