'''
list_functions.py

Author: Max Friedman
'''


import sys
import math
import random
import itertools
import hashlib
import pickle
import functools
import fractions
import tokenize
import io
import typing as ty

tau = 2 * math.pi
phi = (1 + 5 ** 0.5) / 2



class rational:
	'''Create a generator of rational numbers.'''

	def __init__(self, max: int =-1) -> None:
		self.max = max
		self.dir = "up"

	def __iter__(self):
		self.a = 0
		self.b = 1
		return self

	def __next__(self) -> ty.Tuple[int, int]:
		ans = self.a / self.b
		
		if self.a == self.max:
			raise StopIteration
		
		if self.a == 1 and self.dir == "down":
			self.b += 1
			self.dir = "up"
		elif self.b == 1 and self.dir == "up":
			self.a += 1
			self.dir = "down"
		else:
			if self.dir == "down":
				self.a -= 1
				self.b += 1
			if self.dir == "up":
				self.a += 1
				self.b -= 1
				
		return self.a, self.b

	
def lower_input(prompt: ty.Optional[str]=None) -> str:
	'''Call input with the prompt and return the striped lowercase version
	of the input.
	'''

	return input(prompt).strip().lower()

	
def devar(*args: ty.Any) -> ty.Tuple[ty.Any]:
	'''Return the input.'''

	return args


def find_factor(n: int, i: int=2) -> int:
	'''Find the smallest prime factor of n above i.'''

	if i == 2:
		if not n % 2:
			return 2
		i = 3

	sqrt_n = int(n ** .5) + 1
	while i < sqrt_n:
		if not n % i:
			return i
		i += 2
	return n


def factorize(n: int, start: int=2) -> ty.Tuple[int, ...]:
	'''Return a tuple of prime factors of n'''

	factors = []
	while n > 1:
		f = find_factor(n, start)
		n = n // f
		factors.append(f)

	return tuple(factors)


def quad_form(a: float, b: float, c: float) -> ty.Tuple[float, float]:
	'''Return a tuple with the results of the quadratic equation of the
	arguments.'''

	rand = ((b * b) - 4 * a * c) ** .5
	return (-b + rand) / (2 * a), (-b - rand) / (2 * a)


def un_pyth(a: float, c: float) -> float:
	'''Find a side of a right triangle give one leg and the
	hypotanuse.'''

	return ((c * c) - (a * a)) ** .5


def insert_string(main_str: str, insert: str, place: int) -> str:
	'''Insert a given string into another string at a given index.'''

	return "".join(list(main_str).insert(place, insert))


def factorial(n: int) -> int:
	'''Return the factorial of n.'''

	ans = 1
	for i in range(1, n + 1):
		ans = ans * i
	return ans

	
def permute(n: int, r: int) -> int:
	'''Return n permute r.'''

	if r > n:
		raise ValueError("second argument: %d is greater than first argument: %d"%(r,n))
	else:
		return factorial(n) // factorial(n - r)

	
def choose(n: int, r: int) -> int:
	'''Return n choose r.'''

	if r > n:
		raise ValueError("second argument: %d is greater than first argument: %d"%(r,n))
	else:
		return permute(n, r) // factorial(r)


def rand_str(
	length: int=4, charset: ty.Iterable="abcdefghijklmnopqrstuvwxyz") \
	-> str:
	'''Return a random string of length length from the character set
	charset.'''

	return "".join(
		charset[random.randint(
			0,
			len(charset) - 1)] for i in range(length))


def start_substr(substr: str, string: str) -> int:
	'''Find index of first occurance of substr in string.'''

	if substr not in string:
		raise ValueError("Substring not in string.")
	for i in range(len(string)):
		if substr[0] == string[i]:
			start = True
			for j in range(len(substr)):
				if substr[j] != string[i + j]:
					start = False
			if start == True:
				return i


def find_center(item) -> ty.Tuple[float, float]:
	'''Something to do with graphics.'''

	c = a.coords(item)
	if len(c) == 4:
		x = (c[0] + c[2]) / 2
		y = (c[1] + c[3]) / 2
		return x, y
	else:
		raise ValueError


def overlap(
	a: ty.Sequence[float],
	b: ty.Sequence[float]) \
	-> float:
	'''Find the overlap between intervals.'''
	
	return max(0, min(a[1], b[1]) - max(a[0], b[0]))


def num_to_color(number: float, max: float=100) -> str:
	'''Convert an integer to the html format of color.'''
	
	color = colorsys.hls_to_rgb(number / max, 100, 1)
	ans = list(map(lambda c: str(hex(int(c)))[2:], color))
	ans = ["0" + i if len(i) == 1 else i for i in ans]

	return "#" + "".join(ans)


def div(inter: ty.Sequence[ty.Sequence[float]],
	pieces: int) -> ty.Tuple[ty.Tuple[float, float], ...]:
	'''Divide an interval into pieces number of pieces and return it as
	a list of length 2 tuples.'''

	ans = []
	for i in range(pieces):
		first = inter[0] + i * (inter[1] - inter[0]) / pieces
		second = inter[0] + (i + 1) * (inter[1] - inter[0]) / pieces
		ans.append((first, second))
	return ans


def rect(
	par: ty.Sequence[ty.Sequence[float]]=((0, 1),),
	point: str="m",
	y: ty.Callable[[float], float]=lambda a: a)  \
	-> float:
	'''Approximate the integral of y using rectangles.'''

	area = 0
	for i in par:
		if point in ("m","mid","midpoint"):
			x_val = (i[0] + i[1]) / 2
		elif point in ("l", "left", "left end point"):
			x_val = i[0]
		elif point in ("r", "right", "right end point"):
			x_val = i[1]

		area += (i[1] - i[0]) * y(x_val)
	return area


def trap(
	par: ty.Sequence[ty.Sequence[float]]=((0, 1),),
	y: ty.Callable[[float], float]=lambda a: a)  \
	-> float:
	'''Approximate the integral of y using the trapezoid method.'''
	
	area = 0
	for i in par:
		area += (i[1] - i[0]) * (y(i[0]) + y(i[1])) / 2
	return area


def simp(
	par: ty.Sequence[ty.Sequence[float]]=((0, 1),),
	y: ty.Callable[[float], float]=lambda a: a)  \
	-> float:
	'''Use the simpsons method to approximate the integral of y using the
	partitioning of par.
	'''
	
	area = 0
	for i in par:
		area += ((i[1] - i[0]) / 6) * (y(i[0]) + 4 * y((i[0] + i[1]) / 2) + y(i[1]))
	return area


def sigmoid(x: float) -> float:
	'''A simple logistic curve.'''

	return 1 / (1 + e ** (-x))


def comp_abs(x: complex) -> float:
	'''Return the distance to the origin of a complex number.'''

	return (x.real * x.real + x.imag * x.imag) ** .5


def html_color(color: int) -> str:
	'''Convert an integer to the html format of color.'''
	
	ans = list(map(lambda c: str(hex(int(c)))[2:], color))
	ans = ["0" + i if len(i) == 1 else i for i in ans]
	return "#" + "".join(ans)


def sinh(x: float) -> float:
	'''Return the hyperbolic sine of x.'''

	return ((e ** x) - (e ** (-1 * x))) / 2


def cosh(x: float) -> float:
	'''Return the hyperbolic cosine of x.'''
	
	return ((e ** x) + (e ** (-1 * x))) / 2
	

def hype(a: float, b: float, n: int) -> float:
	'''The Hyperoperation sequence implemented recursively.'''

	if n == 0:
		return b + 1
	elif n == 1 and b == 0:
		return a
	elif n == 2 and b == 0:
		return 0
	elif n >= 3 and b == 0:
		return 1
	else:
		return hype(a, hype(a, b - 1, n), n - 1)


def find_indecies(string: str, sub: str) -> int:
	'''Generate the starting indexes of a substing in a string.'''
	
	last = -1
	while 1:
		last = string.find(sub, last + 1)
		if last == -1:
			break
		yield last


def polynomial_factory(*coefficients: float)   \
	-> ty.Callable[[float], float]:
	'''Return a polynomial with coefficients passed to it.'''

	def polynomial(x: float) -> float:
		res = 0
		for index, coeff in enumerate(coefficients):
			res += coeff * x ** index
		return res
	return polynomial


def law_cos(a: float, b: float, c: float, C: float) -> float:
	'''Return the value of the variable that has the value None.'''
	
	if c is None:
		return (a * a + b * b - 2 * a * b * math.cos(C)) ** .5
	elif a is None:
		return ((4 * b * b * math.cos(C) * math.cos(C) - 4 * (b * b - c 
		* c)) ** .5 + 2 * b * math.cos(C)) / 2
	elif b is None:
		return ((4 * a*a * math.cos(C) * math.cos(C) - 4 * (a * a - c
		* c)) ** .5 + 2 * a * math.cos(C)) / 2
	elif C is None:
		return math.acos((a * a + b * b - c * c) / (2 * a * b))


def find_match(s: str) -> ty.Tuple[str, str]:
	'''
	Split a string into two parts. The first part contains the
	string until the first time parentheses are completely matched. The
	second part contains the rest of the string.

	>>> find_match("(4, (5), 3) + 2")
	('(4, (5), 3)', ' + 2')
	'''

	x = 0
	if not s.startswith("("):
		raise ValueError(
			"error '%s' is an invalid input." % s)
				
	for i in range(len(s)):

		# count the parentheses
		if s[i] == "(":
			x += 1
		elif s[i] == ")":
			x -= 1

		if x == 0:

			# left is all the excess characters after
			# the matched parentheses
			# an is the matched parentheses and everything in them
			an = s[:i + 1]
			left = s[i + 1:]

			break

		elif x < 0:
			raise ValueError(
				"error '%s' is an invalid input." % s)

	try:
		return an, left
	except UnboundLocalError:
		raise ValueError("error '%s' is an invalid input." % s)


def brackets(s: str) -> bool:
	'''
	Return True if the parentheses match, False otherwise.
	
	>>> brackets("())")
	False
	
	>>> brackets("(()())")
	True
	
	>>> brackets("w(h)(a()t)")
	True
	'''

	x = 0
	for i in s:
		if i == "(":
			x += 1
		elif i == ")":
			x -= 1
		if x < 0:
			return False
	return not x


def separate(s: str, splitter: str=",") -> ty.Tuple[str, ...]:
	'''
	Split up arguments of a function with commas
	like mod(x, y) or log(x, y) based on where commas that aren't in
	parentheses.
	
	>>> separate("5, 6 , (4, 7)")
	('5', ' 6 ', ' (4, 7)')
	'''

	terms = s.split(splitter)

	new_terms = []
	middle = False
	term = ""
	for i in terms:
		if middle:
			term = term + splitter + i
		else:
			term = i
		x = brackets(term)
		if x:
			new_terms.append(term)
			middle = False
		else:
			middle = True
	return tuple(new_terms)


def sum_multiples(max: int, factors: ty.Iterable[int]) -> int:
	'''Sum the multiples of the factors that are less than max then
	return the value.'''
	
	multiples = set()
	
	for f in factors:
		i = 0
		while i < max:
			multiples.add(i)
			i += f

	return sum(multiples)


def sort_by_length(
	a: ty.Sequence,
	b: ty.Sequence) -> ty.Tuple[
		ty.Sequence,
		ty.Sequence]:
	'''Return the input as a tuple sorted with shortest items first.'''

	if len(a) > len(b):
		return(b, a)
	return(a, b)


def list_union(
	n: ty.List[ty.Any],
	m: ty.List[ty.Any]) -> ty.List[ty.Any]:
	'''Return the smallest list that both lists are subsets of.'''
	
	n, m = sort_by_length(n, m)
	
	m = list(m)
	
	for i in n:
		if m.count(i) < n.count(i):
			m.append(i)
	return m


def lcm(a: int, b: int) -> int:
	'''Find the lowest common multiple of two numbers.'''
	
	alist = factorize(a)
	blist = factorize(b)
	
	return functools.reduce(lambda a, b: a * b, list_union(alist, blist))


def detect_palindrome(n: ty.Any) -> bool:
	'''Return True if the string form of an object is a palindrome'''
	
	n = str(n)
	
	return bool(n == "".join(reversed(n)))


def find_largest_adjacent_product(digits, number):
	'''Return the largest number which can be created by multipling
	adjacent digits together.'''

	# I think something is wrong with the argument names
	t = 0
	for i in range(len(number) + 1 - digits):
		n = functools.reduce(
			lambda a, b: int(a) * int(b),
			tuple(number[i:i + digits]))
		if n > t:
			t = n
			d = number[i:i + digits]
	return t, d


def check_equal(iterator: ty.Iterable) -> bool:
	'''Check if all elements of a list are equal.'''

	return len(set(iterator)) <= 1 # content must be hashable


def convert_to_dict(lst: ty.Iterable) -> ty.Dict[ty.Any, int]:
	'''Convert to dictonary with elemnts as keys and count as value.'''

	d = {}
	for i in lst:
		if i in d:
			d[i] = d[i] + 1
		else:
			d[i] = 1
	return d


def sum_digits(n: int) -> int:
	'''Sum the digits of a number.'''

	digits = list(str(n))
	return sum(map(lambda x: int(x), digits))


def collaspe_frac(it: ty.Iterable[float]) -> fractions.Fraction:

	x = fractions.Fraction(0)
	for count, val in enumerate(reversed(it)):

		if count == len(it) - 1:
			return val + x

		if not count:
			x = fractions.Fraction(1, val)
		else:
			x = 1 / (val + x)


def check_prime(n: int) -> bool:
	'''Return True if a number is prime.'''
	
	if n == 2:
		return True
	elif not n%2:
		return False
	elif n == 1:
		return False

	i = 3
	sqrt_n = int(n**.5)
	while i <= sqrt_n:
		if not n%i:
			return False
		i += 2
	return True


def totient(n: int) -> int:
    result = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
        i += 1
    if n > 1:
        result -= result // n
    return result


dict = {
	"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
}


def longest(s: str, c: str) -> int:
	'''Find how many copies of c are at the begining of s.
	Assumes c is a single character.'''

	count = 1
	while 1:
		if s[:count] == c * count:
			count += 1
		else:
			return count - 1


def roman_2_int(s: str) -> int:
	'''Convert a Roman numeral to an int.'''
	
	total = 0
	
	if not s:
		return 0
	if len(s) == 1:
		return dict[s]
	start = s[0]
	

	if start in ("V", "L", "D"):
		return roman_2_int(s[1:]) + dict[start]
	elif start == "I" and s[1] in ("V", "X"):
		return roman_2_int(s[2:]) + dict[s[1]] - dict[start]
	elif start == "X" and s[1] in ("L", "C"):
		return roman_2_int(s[2:]) + dict[s[1]] - dict[start]
	elif start == "C" and s[1] in ("D", "M"):
		return roman_2_int(s[2:]) + dict[s[1]] - dict[start]
	elif start in ("I", "X", "C", "M"):
		count = longest(s, start)
		total += dict[start] * count
		return total + roman_2_int(s[count:])


def int_2_roman(n: int) -> str:
	'''Convert and integer to a Roman numeral.'''

	s = ""

	while n >= 1000:
		s += "M"
		n -= 1000
	if n >= 900:
		s += "CM"
		n -= 900
	if n >= 500:
		s += "D"
		n -= 500
	if n >= 400:
		s += "CD"
		n -= 400
	while n >= 100:
		s += "C"
		n -= 100
	if n >= 90:
		s += "XC"
		n -= 90
	if n >= 50:
		s += "L"
		n -= 50
	if n >= 40:
		s += "XL"
		n -= 40
	while n >= 10:
		s += "X"
		n -= 10
	if n == 9:
		s += "IX"
		return s
	if n >= 5:
		s += "V"
		n -= 5
	if n == 4:
		s += "IV"
		return s
	while n >= 1:
		s += "I"
		n -= 1
	return s


def reduce_roman(s: str) -> str:
	return int_2_roman(roman_2_int(s))


def sortby(
	somelist: ty.Iterable[ty.Iterable],
	n: int) -> list:
	'''Sort a list by its nth element.'''

	nlist = [(x[n], x) for x in somelist]
	nlist.sort()
	return [val for (key, val) in nlist]


def primes() -> ty.Iterable[int]:
	'''Generate a list of primes.'''

	count = 3
	yield 2
	while 1:
		if check_prime(count):
			yield count
		count += 2


def factor(n: int) -> ty.Set[int]:
	'''Return a list of all factors of n.'''

	factors = set()
	for i in range(1, int(n ** .5) + 1):
		if not n % i:
			factors.add(i)
			factors.add(n // i)
	return factors


def triangle() -> ty.Iterable[int]:
	'''Return the triangle numbers.'''

	t = 1
	c = 2
	while 1:
		yield t
		t += c
		c += 1


def join_format(s: str, iterable: ty.Iterable[str]) -> str:

	return ''.join(map(lambda a: s.format(a), iterable))


def isonly(n: ty.Iterable, only: ty.Iterable) -> bool:
	'''Check if n is comprized solely of elements found in only.'''

	for i in n:
		if i not in only:
			return False
	return True

class DummyFile(io.IOBase):
	def __init__(self, content):
		super(DummyFile, self).__init__()
		self.content = content
	def read(self, *args):
		return self.content.encode("utf-8")


def split_into_tokens(s):
	'''Split a string into tokens.'''
	
	if s[-1] != "\n":
		s += "\n"
	
	file = DummyFile(s)
	token = tokenize.tokenize(file.readline)
	
	token_info = token.send(None)
	tokens = []
	start = token_info.start
	notend = True
	while notend:
		token_info = token.send(None)
		if token_info.start[1] == token_info.start[1]:
			notend = False
			break
		tokens.append(token_info)
	file.close()
	return tokens


