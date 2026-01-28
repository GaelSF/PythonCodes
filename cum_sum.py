import numpy as np
import matplotlib.pyplot as plt

#Make dictionary
#x = {i: np.random.rand() for i in range(7+1)}

# Cumulative sum for 50 random numbers
#z = np.random.randint(10,600,30)
#z_cum = z.cumsum()
#print(z)
#print()
#print(z_cum)

# Graph cum sum
#plt.plot(z_cum)
#plt.show()

for i in range(4):
	u = np.random.randint(250,300,30)
	v = np.random.randint(190,225,30)

#print(u)
#print(v)
	u_cum = u.cumsum()
	v_cum = v.cumsum()

	p=v_cum/u_cum

#print(p)

	plt.plot(p)
	plt.ylim(0,1)
plt.show()
