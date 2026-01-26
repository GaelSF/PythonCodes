import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,60)
#print(x)
y = np.exp(-x)

plt.plot(x, y)
plt.show()
