import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,400)

mu = 0.0
std = 0.1
size = 400
y_rand = np.random.normal(mu, std, size)

y = np.exp(-x) + y_rand

plt.plot(x, y)
plt.plot(x, np.exp(-x))
plt.show()
