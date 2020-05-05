from fractions import Fraction


def return_same_class(cls):
	"""Wrap the methods in 'methods' so that they will return an instance of
	the class that they were called from, not any base classes"""

	def wrap(func):
		"""Wrap func so that it returns the type of the first argument"""

		return lambda self, *args, **kwargs: self.__class__(func(self, *args, **kwargs))

	methods = (
		"__add__", "__radd__",
		"__sub__", "__rsub__",
		"__mul__", "__rmul__",
		"__truediv__", "__rtruediv__",
		"__mod__", "__rmod__",
		"limit_denominator"
	)

	for method in methods:
		wrapped = wrap(getattr(cls, method))
		setattr(cls, method, wrapped)

	return cls

def limit_float_denominators(method, cls):
	"""Wrap method so that the denominators of floats are limited when used
	in operations"""

	def func(self, other):
		"""If other is a float convert it the the type of self and call
		limit_denominator on it, before calling method on it. Otherwise proced
		as normal"""

		if isinstance(other, float):
			return getattr(self, method)(self.__class__(other).limit_denominator())

		return getattr(super(cls, self), method)(other)
	return func

def overload_math_dunder_methods(func):
	"""Create a decorator that wraps methods of a class in func"""

	def decorator(cls):
		"""Wrap the methods in 'methods' in func"""

		methods = (
			"__add__", "__radd__",
			"__sub__", "__rsub__",
			"__mul__", "__rmul__",
			"__truediv__", "__rtruediv__",
			"__mod__", "__rmod__"
		)

		for method in methods:
			f = func(method, cls)
			setattr(cls, method, f)

		return cls
	return decorator

@return_same_class
@overload_math_dunder_methods(limit_float_denominators)
class SwitchFracBase(Fraction):
	"""The base number class for Switch"""

	def __new__(cls, *args, base=10, **kwargs):
		if base == 10:
			return super().__new__(cls, *args, **kwargs)
		return super().__new__(cls, cls._from_base(*args, base))

	@staticmethod
	def _from_base(n, base=10):
		if base <= -1:
			if base == -1:

				if any(l not in "1_" for l in n):
					raise ValueError("Can only have '1' and '_' in unary number")
				else:
					return n.count("1")

			if "." in n:
				integer, decimal = n.split(".")
			else:
				integer = n
				decimal = ""

			sign = 1
			if integer.startswith("-"):
				integer = integer[1:]
				sign = -1

			int_part = 0
			for place, digit in enumerate(reversed(integer)):
				int_part += int(digit, -base) * base ** place

			dec_part = 0
			for index, digit in enumerate(decimal):
				dec_part += float(int(digit, -base)) / base ** (index + 1)

			return sign * (int_part + dec_part)

		if base == 1:

			sign = 1
			if n.startswith("-"):
				integer = integer[1:]
				sign = -1

			if any(l not in "1_" for l in n):
				raise ValueError("Can only have '1' and '_' in unary number")
			else:
				return sign * n.count("1")

		if "." in n:
			integer, decimal = n.split(".")
		else:
			integer = n
			decimal = ""

		int_part = int(integer, base)

		dec_part = 0
		for index, digit in enumerate(decimal):
			dec_part += float(int(digit, base)) / base ** (index + 1)

		return int_part + dec_part
		

	def __str__(self):
		if self.denominator == 1:
			return str(self.numerator)
		else:
			return str(self.numerator / self.denominator)

	def __repr__(self):
		if self.denominator == 1:
			return str(self.numerator)
		else:
			return str(self.numerator / self.denominator)

	# I forget what raised an error when this wasn't there
	# I should figure it out so I know if it is safe to deleter
	# Don't delete before then. Its not hurting anything :)
	def is_integer(self):
		return self.denominator == 1


class SwitchFrac(SwitchFracBase):
	"""Number class for Switch"""

	def __mul__(self, other):
		"""Multiplication by strings and other sequences should work if self
		is a whole number"""

		try:
			return super().__mul__(other)
		except TypeError:
			if self.denominator == 1:
				return self.numerator * other
			else:
				raise

	def __rmul__(self, other):
		"""Multiplication by strings and other sequences should work if self
		is a whole number"""

		try:
			return super().__rmul__(other)
		except TypeError:
			if self.denominator == 1:
				return other * self.numerator
			else:
				raise




if __name__ == "__main__":
	print(SwitchFrac("-191.9", base=-10))
	print(type(SwitchFrac("191.9", base=-10)))
