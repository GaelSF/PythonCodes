import numpy as np
import matplotlib.pyplot as plt

#Make dictionary
x = {i: np.random.rand() for i in range(7+1)}

# Cumulative sum for 50 random numbers
z = np.random.rand(50)
z_cum = z.cumsum()
print(z)

# Graph cum sum
plt.plot(z_cum)
plt.show()


