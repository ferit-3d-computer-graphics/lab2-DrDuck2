import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

grid_size = 20  
x = np.linspace(-3, 3, grid_size)
y = np.linspace(-3, 3, grid_size)
z = np.linspace(-3, 3, grid_size)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

blob1 = np.exp(-((X - 0.5)**2 + (Y - 0.5)**2 + (Z - 0.5)**2) / 0.5)
blob2 = np.exp(-((X + 0.5)**2 + (Y + 0.5)**2 + (Z + 0.5)**2) / 0.5)
sinusoid = 0.5 * (np.sin(X * 2) + np.sin(Y * 2) + np.sin(Z * 2))

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

view_elev = 30
view_azim = 45
ax.view_init(elev=view_elev, azim=view_azim)

def on_rotate(event):
    global view_elev, view_azim
    view_elev = ax.elev
    view_azim = ax.azim
    
fig.canvas.mpl_connect('motion_notify_event', on_rotate)

def update(frame):
    global view_elev, view_azim
    
    t = frame / 30.0
    tb1 = 0.2 + 0.1 * np.sin(t * 2 * np.pi)
    tb2 = 0.3 + 0.1 * np.sin(t * 2 * np.pi + np.pi/2)
    ts = 0.6 + 0.1 * np.sin(t * 2 * np.pi + np.pi)
    
    mask_blob1 = blob1 > tb1
    mask_blob2 = np.logical_and(blob2 > tb2, np.logical_not(mask_blob1))
    mask_sinusoid = np.logical_and(sinusoid > ts, 
                               np.logical_not(np.logical_or(mask_blob1, mask_blob2)))
    
    voxel_array = mask_blob1 | mask_blob2 | mask_sinusoid
    
    colors = np.empty(voxel_array.shape, dtype=object)
    colors[mask_blob1] = 'red'
    colors[mask_blob2] = 'green'
    colors[mask_sinusoid] = 'blue'
    
    stored_elev = view_elev
    stored_azim = view_azim
    
    ax.clear()
    ax.voxels(voxel_array, facecolors=colors, edgecolor='k', alpha=0.7)
    
    ax.set_title(f'Thresholds: R={tb1:.2f}, G={tb2:.2f}, B={ts:.2f}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    ax.view_init(elev=stored_elev, azim=stored_azim)

ani = FuncAnimation(fig, update, frames=30, interval=200, blit=False)
plt.show()
