# log algorithm

import matplotlib.pyplot as plt
import math

ln2 = 0.69314718056

def log(arg, base):
	m, e = math.frexp(arg)
	
	x = (m - 1) / (m + 1)
	lnm = 2 * (x + (x**3) / 3 + (x ** 5) / 5)
	
	return lnm + e * ln2




plt.plot([log(i*.01, 1) - math.log(i*.01) for i in range(100, 200)])
plt.ylabel('some numbers')
plt.show()

print(log(3.0, 1))
