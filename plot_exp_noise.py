import numpy as np
import matplotlib.pyplot as plt


def func_noise(a, b, mu, std, size):
	x = np.linspace(a, b, size)
	y_x = np.exp(-x)
	y_noise = np.random.normal(mu, std, size)
	y = y_x + y_noise
	return x, y_x, y

x, y_x, y = func_noise(0, 10, 0.0, 0.1, 100)

plt.plot(x, y_x, 'r-')
plt.plot(x, y)
plt.show()
