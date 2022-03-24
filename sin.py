# sin algorithm

import matplotlib.pyplot as plt
import math

pi = math.pi

def sin(x):
	return 16*x*(pi-x) / (5 * pi * pi - 4 * x * (pi - x))



plt.plot([sin(i*.001) - math.sin(i*.001) for i in range(1000)])
plt.ylabel('some numbers')
plt.show()

#print(sin(pi / 6))
