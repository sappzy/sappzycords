import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array([10,20,70,200])
ypoints=np.array([10,12,14,16])
plt.plot(xpoints,ypoints,marker='o')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('line plot with markers')
plt.show()
