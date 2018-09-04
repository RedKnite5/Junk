#   vector_hw.py

# cd C:\Users\Max\Documents\Python\ReCalc
# cd C:\Users\Max\Documents\Python\Junk

from math import acos, pi

def magnitude(v: ty.Tuple[float, ...]) -> float:
	'''Find the magnitude of a vector'''

	return sum(i * i for i in v) ** .5

def dot(v1: ty.tuple[float, ...], v2: ty.Tuple[float, ...]) -> float:
	'''Return the dot product of the inputs'''

	return sum(i * k for i, k in zip(v1, v2))

def find_angle(
	v1: ty.Tuple[float, ...],
	v2: ty.Tuple[float, ...]) -> float:
	'''Find the angle between two vectors'''

	return acos(dot(v1, v2) / (magnitude(v1) * magnitude(v2)))

def rad_to_deg(n: float) -> float:
	'''Convert from radians to degrees'''

	return n * 180 / pi

def proj(
	a: ty.Tuple[float, ...],
	b: ty.Tuple[float, ...]) -> ty.Tuple[float, ...]:
	'''Project vector a on to vector b'''

	scalar = dot(a, b) / dot(b, b)
	return tuple(map(lambda a: a * scalar, b))
	
a = eval(input("Input a vector\n"))
b = eval(input("Input a second vector\n"))
v = proj(a, b)
print(v, magnitude(v))
