import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-3, 3)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Scene with Animated Object')

ax.plot([0, 3], [0, 0], [0, 0], 'r-', linewidth=2)  
ax.plot([0, 0], [0, 3], [0, 0], 'g-', linewidth=2)  
ax.plot([0, 0], [0, 0], [0, 3], 'b-', linewidth=2)  

cube_vertices = np.array([
    [0.5, 0.5, 0.5], [1.5, 0.5, 0.5], [1.5, 1.5, 0.5], [0.5, 1.5, 0.5],
    [0.5, 0.5, 1.5], [1.5, 0.5, 1.5], [1.5, 1.5, 1.5], [0.5, 1.5, 1.5]
])
cube_edges = [
    [0,1], [1,2], [2,3], [3,0],
    [4,5], [5,6], [6,7], [7,4],
    [0,4], [1,5], [2,6], [3,7]
]
for edge in cube_edges:
    ax.plot3D(*cube_vertices[edge].T, color='yellow')

point, = ax.plot([], [], [], 'mo', markersize=10)

def update(frame):
    angle = np.radians(frame)
    x = 2 * np.cos(angle)
    y = 2 * np.sin(angle)
    point.set_data([x], [y])
    point.set_3d_properties([0])
    return point,

ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)
ax.view_init(elev=20, azim=45)
plt.show()
