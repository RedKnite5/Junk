from math import pi


def Z(W):
	w = 2*pi*W
	c = 0.33 * 10**(-6)
	L = 100 * 10**(-3)
	r1 = 1000
	r2 = 240

	b1 = -1j/(c*w)
	b2 = r2 + L*w*1j

	#impedance
	return b1*b2/(b1+b2) + r1

freq = [100, 500, 1000, 2000]
for f in freq:
	z = Z(f)
	r, i = z.real, z.imag
	print(f"{round(r)} + {round(i)}i")




