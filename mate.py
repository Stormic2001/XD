import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

u = np.linspace(0, 6 * np.pi, 100)
v = np.linspace(-1, 1, 30)
U, V = np.meshgrid(u, v)
X = U
Y = np.cos(U) + V
Z = np.sin(U) + V

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.show()
