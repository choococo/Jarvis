import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x = np.random.randn(100)
y = np.random.randn(100)
z = np.random.randn(100)
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x,y,z,c="r",marker="p",label = "boy")
plt.legend()
plt.show()
