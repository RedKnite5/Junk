import math

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


#x = np.linspace(0, 10, 5000)
x = np.arange(2.5, 4.5, 0.0001)


def func(a):
	f = math.e ** 2 * a
	f = f * np.cos(2 * a * math.pi) - f
	f = math.e ** f
	f = (a ** 1.1) * f
	f = (math.e ** f) - 1
	return f


def F(x):
	res = np.zeros_like(x)
	for i, val in enumerate(x):
		try:
			y, err = integrate.quad(func, 0, val)
			res[i] = y
		except:
			res[i] = func(val)
	return res

y = func(x)
plt.plot(x, F(x))
plt.plot(x, np.log(y))
plt.show()

