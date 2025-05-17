import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

central_object = np.array([0, 0, 0])

satellite_offsets = np.array([
    [3, 0, 0],   
    [0, 4, 0],    
    [0, 0, 5]     
], dtype=np.float32)

rotation_speeds = np.array([0.02, 0.015, 0.01], dtype=np.float32)

def rotation_matrix_z(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [c, -s, 0],
        [s, c, 0],
        [0, 0, 1]
    ], dtype=np.float32)

def compute_rotated_positions(frame):
    rotated_positions = []
    for i, offset in enumerate(satellite_offsets):
        angle = rotation_speeds[i] * frame
        R = rotation_matrix_z(angle)
        rotated_pos = R @ offset + central_object
        rotated_positions.append(rotated_pos)
    return np.array(rotated_positions, dtype=np.float32)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

satellites = central_object + satellite_offsets

central_plot = ax.scatter(*central_object, color='white', s=200, label='Central Object')
satellites_plot = ax.scatter(satellites[:, 0], satellites[:, 1], satellites[:, 2], 
                            color='blue', s=100, label='Satellites')

ax.scatter([2], [2], [1], color='blue', s=80, alpha=0.5)

ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_zlim(-6, 6)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Rotating Satellites Around Central Object')
ax.legend()

def update(frame):
    new_positions = compute_rotated_positions(frame)
    satellites_plot._offsets3d = (new_positions[:, 0], new_positions[:, 1], new_positions[:, 2])
    return satellites_plot,

ani = FuncAnimation(fig, update, frames=range(360), interval=50, blit=False)
plt.show()