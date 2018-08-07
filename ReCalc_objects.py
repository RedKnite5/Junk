# -*- coding: utf-8 -*-

'''
Classes and functions for ReCalc
'''

import re
from decimal import Context, Decimal

# import tkinter if installed
try:
	import tkinter as tk
	from tkinter import filedialog
	from _tkinter import TclError
	from PIL import ImageTk
except ModuleNotFoundError:
	pass


__all__ = [
	"Unit", "compile_ignore_case", "CalculatorError",
	"NonRepeatingList", "Graph", "check_if_ascii", "float_to_str",
	"check_if_float", "find_match", "separate", "sort_by_length"
]

def double_list(l):
	return([i for s in ((i, i) for i in l) for i in s])

def flatten(l):
	return((i for s in l for i in s))

def brackets(s):
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
			return(False)
	return(not x)


ctx = Context()
ctx.prec = 17

def compile_ignore_case(pattern):
	'''
	Call re.compile with the IGNORECASE flag.
	'''

	return(re.compile(pattern, flags = re.I))


def check_if_ascii(s):
	try:
		s.encode("ascii")
		return(True)
	except UnicodeEncodeError:
		return(False)


def float_to_str(f):
	'''
	Convert the given float to a string,
	without resorting to scientific notation.

	>>> float_to_str(3.0030)
	'3.003'
	'''

	d1 = ctx.create_decimal(repr(float(f)))
	string = format(d1, "f")
	if string[-2:] == ".0":
		return string[:-2]
	return string


def check_if_float(x):
	'''
	Test if a object can be made a float.

	>>> check_if_float("4.5")
	True

	>>> check_if_float("this")
	False
	'''

	try:
		float(x)
		return(True)
	except (ValueError, TypeError):
		return(False)


def find_match(s):
	'''
	Split a string into two parts. The first part contains the
	string until the first time parentheses are completely matched. The
	second part contains the rest of the string.

	>>> find_match("(4, (5), 3) + 2")
	('(4, (5), 3)', ' + 2')
	'''

	x = 0
	if not s.startswith("("):
		raise CalculatorError(
			"Error '%s' is an invalid input, must start with '('" % s)

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
			an = s[:i+1]
			left = s[i+1:]

			break

		elif x < 0:
			raise CalculatorError(
				"'%s' is an invalid input. Parentheses do "
				"not match." % s)

	try:
		return(an, left)
	except UnboundLocalError:
		raise CalculatorError(
			"'%s' is an invalid input to find_match." % s)


def separate(s):
	'''
	Split up arguments of a function with commas
	like mod(x, y) or log(x, y) based on where commas that aren't in
	parentheses.

	>>> separate("5, 6 , (4, 7)")
	('5', ' 6 ', ' (4, 7)')
	'''

	terms = s.split(",")

	new_terms = []
	middle = False
	term = ""
	for i in terms:
		if middle:
			term = term + "," + i
		else:
			term = i
		x = brackets(term)
		if x:
			new_terms.append(term)
			middle = False
		else:
			middle = True
	return(tuple(new_terms))


def sort_by_length(l):
	return(tuple(reversed(sorted(l))))


def enumerate2(xs, start=0, step=1):
    for x in xs:
        yield (start, x)
        start += step


def make_unit_list(
	unit,
	abb,
	Range  = (-9, 9),
	centi = True,
	deci = False,
	deca = False,
	hecto = False,
	**kwargs):
	'''
	Make a list of units with prefixes and their multipliers.
	'''

	u = [
		"yocto" + unit, "y" + abb,
		"zepto" + unit, "z" + abb,
		"atto" + unit, "a" + abb,
		"femto" + unit, "f" + abb,
		"pico" + unit, "p" + abb,
		"nano" + unit, "n" + abb,
		"micro" + unit, "µ" + abb,
		"milli" + unit, "m" + abb,
		"kilo" + unit, "k" + abb,
		"mega" + unit, "M" + abb,
		"giga" + unit, "G" + abb,
		"tera" + unit, "T" + abb,
		"peta" + unit, "P" + abb,
		"exa" + unit, "E" + abb,
		"zetta" + unit, "Z" + abb,
		"yotta" + unit, "Y" + abb,
	]
	m = [
		1e24, 1e21, 1e18, 1e15, 1e12, 1e9, 1e6, 1e3,
		1e-3, 1e-6, 1e-9, 1e-12, 1e-15, 1e-18, 1e-21, 1e-24,
	]

	start = (int(Range[0] / 3) + 8)
	end = int(Range[1] / 3) + 8

	un = u[start * 2:end * 2]
	mu = m[start:end]

	if centi:
		un.extend(("centi" + unit, "c" + abb))
		mu.append(1e2)
	if deci:
		un.extend(("deci" + unit, "d" + abb))
		mu.append(1e1)
	if deca:
		un.extend(("deca" + unit, "da" + abb))
		mu.append(1e-1)
	if hecto:
		un.extend(("hecto" + unit, "h" + abb))
		mu.append(1e-2)

	for prefix in kwargs:
		if (prefix + unit) in un and not kwargs[prefix]:
			index = un.index(prefix + unit)
			un.pop(index)
			un.pop(index)
			mu.pop(index // 2)
		elif (prefix + unit) not in un and kwargs[prefix]:
			index = u.index(prefix + unit)
			un.extend((u[index], u[index + 1]))
			mu.append(m[index // 2 -1])

	return(un, mu)


class CalculatorError(Exception):
	pass


class Unit(object):
	'''
	A class that represents different quantities
	'''

	distance_units = (
		"kilometers", "km",
		"centimeters", "cm",
		"millimeters", "mm",
		"inches", "in",
		"feet", "ft",
		"yards", "yd",
		"miles", "mi",
		"mils", "mil",
		"rods", "poles",
		"nautical miles", "nmi",
	)
	distance_mult = (
		0.001, 100, 1000, 39.370078740157, 3.2808398950131,
		1.0936132983377, 0.00062137119223733, .039370078740157,
		5.029, 0.000539957,
	)

	mass_units = (
		"grams", "g",
		"pounds-mass", "lbm",
		"milligrams", "mg",
		"ounces", "oz",
		"tons", "tons",
		"micrograms", "µg",
		"tonnes", "t",
	)
	mass_mult = (
		1000, 2.2046226218, 1e6, 35.274, 0.00110231, 1e12,
		0.001,
	)

	time_units = (
		"minutes", "min",
		"hours", "hr",
		"days", "d",
		"weeks", "wk",
		"years", "yr",
		"milliseconds", "ms",
		"nanoseconds", "ns",
	)
	time_mult = (
		1 / 60, 1 / 3600, 1 / 86400, 1 / 604800, 1 / 31557600,
		1000, 1000000000,
	)

	volume_units = (
		"milliliters", "mL",
		"centimeters cubed", "cm^3",
		"feet cubed", "ft^3",
		"gallons", "gal",
		"kiloliters", "kL",
		"fluid ounces", "fl oz",
		"pints", "pt",
		"quarts", "qt",
		"drams", "dr",
		"tablespoons", "tblsp",
		"teaspoons", "tsp",
		"microliters", "µL",
		"deciliters", "dL"
	)
	volume_mult = (
		1000, 1000, 0.0353147, 0.264172, .0001, 33.814, 2.11338,
		1.05669, 270.512, 67.628, 202.884, 1e6, 10,
	)

	voltage_units, voltage_mult = make_unit_list("volts", "V")

	energy_units = (
		"calories", "cal",
		"kilocalories", "Cal",
		"kilojoules", "kJ",
		"foot-pounds", "ft lb",
		"watt-hours", "Wh",
		"kilowatt-hours", "kWh",
		"British thermal units", "BTU",
		"ergs", "erg",
	)
	energy_mult = (
		0.239006, 0.000239006, 0.001, 0.737562, 1/3600,
		1/3600000, 0.000947817, 1e+7,
	)

	area_units = (
		"square feet", "ft^2",
		"square inches", "in^2",
		"square yards", "yd^2",
		"hectares", "ha",
		"acres", "ac",
		"square miles", "mi^2",
		"square kilometers", "km^2",
	)
	area_mult = (
		10.7639, 1550, 1.1959876543, 0.0001, 0.000247105, 0.0000003861,
		1e-6,
	)

	frequency_units, frequency_mult = make_unit_list("hertz", "Hz")

	pressure_units, pressure_mult = make_unit_list("pascals", "Pa")
	pressure_units.extend((
		"atmospheres", "Atm",
		"bars", "Bar",
		"torrs", "Torr",
	))
	pressure_mult.extend((
		0.0000098692, 0.00001, 0.00750062,
	))

	speed_units = (
		"kilometers-per-hour", "km/h",
		"feet-per-second", "ft/s",
		"miles-per-hour", "mi/h",
		"knots", "kn",
	)
	speed_mult = (
		3.6, 3.28084, 2.23694, 1.94384,
	)

	acceleration_units = (
		"feet-per-second-squared", "ft/s^2",
	)
	acceleration_mult = (
		3.2808399,
	)

	current_units, current_mult = make_unit_list("amperes", "A")

	resistance_units, resistance_mult = make_unit_list("-ohm", "Ω")

	force_units, force_mult = make_unit_list("newtons", "N")
	force_units.extend((
		"pounds-force", "lbf",
	))
	force_mult.extend((
		0.224809,
	))

	intensity_units, intensity_mult = make_unit_list("candela", "cd")

	temp_units = (
		"degrees-Celsius", "°C",
		"degrees-Fahrenheit", "°F",
	)
	# special case for temp because you also have to add
	temp_mult = tuple([1,] * (len(temp_units) // 2))

	lumen_flux_units, lumen_flux_mult = make_unit_list(
		"lumens", "lm",
		Range = (0, 24),
		hecto = True)

	illuminance_units, illuminance_mult = make_unit_list("lux", "lx")

	power_units, power_mult = make_unit_list(
		"watts", "W",
		Range = (-15, 24))
	power_units.extend((
		"ergs-per-second", "erg/s",
		"horsepower", "hp",
		"metric-horsepower", "PS",
		"poncelets", "p",
	))
	power_mult.extend((
		1e7, 0.00134102, 0.001359621617, 0.001019716213,
	))

	conductance_units, conductance_mult = make_unit_list(
		"siemens", "S",
		Range = (-12, 6))

	charge_units, charge_mult = make_unit_list(
		"coulombs", "C",
		Range = (-12, 9), centi = False)
	charge_units.extend((
		"ampere-hours", "Ah",
	))
	charge_mult.extend((
		1/3600,
	))

	capacitance_units, capacitance_mult = make_unit_list(
		"farad", "F",
		Range = (-12, 3),
		deca = True,
		hecto = True)

	inductance_units, inductance_mult = make_unit_list(
		"henry", "H",
		Range = (-12, 9))

	conductivity_units, conductivity_mult = ((), ())

	magnetic_field_units, magnetic_field_mult = make_unit_list(
		"teslas", "T",
		Range = (-9, 6),
		centi = False)
	gauss_u, gauss_m = make_unit_list("gauss", "G", Range = (-9, 3))
	magnetic_field_units.extend(gauss_u + ["gauss", "G"])
	magnetic_field_mult.extend(list(map(lambda a: a * 1e4, gauss_m)) + [1e4])

	base_units = (
		"meters", "m",
		"seconds", "s",
		"kilograms", "kg",
		"liters", "L",
		"volts", "V",
		"joules", "J",
		"square meters", "m^2",
		"hertz", "Hz",
		"pascals", "Pa",
		"meters-per-second", "m/s",
		"meters-per-second-squared", "m/s^2",
		"amperes", "A",
		"ohm", "Ω",
		"newtons", "N",
		"candela", "cd",
		"kelvin", "K",
		"lumens", "lm",
		"lux", "lx",
		"watts", "W",
		"siemens", "S",
		"coulombs", "C",
		"farad", "F",
		"henry", "H",
		"siemens-per-meter", "S/m",
		"teslas", "T",
	)
	nonbase_units = {
		"distance": distance_units,
		"time": time_units,
		"mass": mass_units,
		"volume": volume_units,
		"voltage": voltage_units,
		"energy": energy_units,
		"area": area_units,
		"frequency": frequency_units,
		"pressure": pressure_units,
		"speed": speed_units,
		"acceleration": acceleration_units,
		"current": current_units,
		"resistance": resistance_units,
		"force": force_units,
		"intensity": intensity_units,
		"temperature": temp_units,
		"lumninous flux": lumen_flux_units,
		"illuminace": illuminance_units,
		"power": power_units,
		"conductance": conductance_units,
		"electric charge": charge_units,
		"capacitance": capacitance_units,
		"inductance": inductance_units,
		"conductivity": conductivity_units,
		"magnetic flux density": magnetic_field_units,
	}
	multipliers = {
		"distance": distance_mult,
		"time": time_mult,
		"mass": mass_mult,
		"volume": volume_mult,
		"voltage": voltage_mult,
		"energy": energy_mult,
		"area": area_mult,
		"frequency": frequency_mult,
		"pressure": pressure_mult,
		"speed": speed_mult,
		"acceleration": acceleration_mult,
		"current": current_mult,
		"resistance": resistance_mult,
		"force": force_mult,
		"intensity": intensity_mult,
		"temperature": temp_mult,
		"lumninous flux": lumen_flux_mult,
		"illuminace": illuminance_mult,
		"power": power_mult,
		"conductance": conductance_mult,
		"electric charge": charge_mult,
		"capacitance": capacitance_mult,
		"inductance": inductance_mult,
		"conductivity": conductivity_mult,
		"magnetic flux density": magnetic_field_mult,
	}

	unit_types = {}
	for index, unit_type in enumerate2(nonbase_units.keys(), step = 2):
		temp_dict = (lambda l, t: {i: t for i in l})(
			nonbase_units[unit_type],
			unit_type)
		temp_dict.update({base_units[index]: unit_type, base_units[index + 1]: unit_type})
		unit_types.update(temp_dict)

	del distance_units, mass_units, time_units, volume_units
	del voltage_units, energy_units, area_units, frequency_units
	del pressure_units, speed_units, acceleration_units, current_units
	del resistance_units, force_units, intensity_units, temp_units
	del lumen_flux_units, power_units, conductance_units, charge_units
	del capacitance_units

	del distance_mult, mass_mult, time_mult, volume_mult, voltage_mult
	del energy_mult, area_mult, frequency_mult, pressure_mult
	del speed_mult, acceleration_mult, current_mult, resistance_mult,
	del force_mult, intensity_mult, temp_mult, lumen_flux_mult
	del illuminance_mult, power_mult, conductance_mult, charge_mult
	del capacitance_mult

	for i in multipliers:
		multipliers[i] = double_list(map(Decimal, multipliers[i]))

	from_base_funcs = {unit: lambda a: a for unit in base_units}
	to_base_funcs = {}
	for unit, mult in zip(
		flatten(nonbase_units.values()),
		flatten(multipliers.values())):

		from_base_funcs.update({unit: lambda a, c = mult: a * c})
		to_base_funcs.update({unit: lambda a, c = mult: a / c})

	var273 = Decimal(273.15)
	var95 = Decimal(9 / 5)
	var32 = Decimal(32)

	# special case stuff for temp
	from_base_funcs.update({
		"degrees-Celsius": lambda a, v2=var273: a - v2,
		"°C": lambda a, v2=var273: a - v2,
		"degrees-Fahrenheit": lambda a, v2=var273, v9=var95, v3=var32:\
			(a - v2) * v9 + v3,
		"°F": lambda a, v2=var273, v9=var95, v3=var32:\
			(a - v2) * v9 + v3,
	})
	to_base_funcs.update({
		"degrees-Celsius": lambda a, v2=var273: a + v2,
		"°C": lambda a, v2=var273: a + v2,
		"degrees-Fahrenheit": lambda a, v2=var273, v9=var95, v3=var32:\
			(a - v3) / v9 + v2,
		"°F": lambda a, v2=var273, v9=var95, v3=var32:\
			(a - v3) / v9 + v2,
	})
	
	del var273, var95, var32

	def __init__(self, amount, type):
		self.type = type
		self.amount = Decimal(amount)

	def __repr__(self):
		return("Unit({a} {u})".format(a = self.amount, u = self.type))

	def __str__(self):
		return("{a} {u}".format(a = self.amount, u = self.type))

	@staticmethod
	def compairable(this, other):
		return(Unit.unit_types[this] == Unit.unit_types[other])

	def convert_to(self, new):
		'''
		Change what unit the quantity is expressed as.
		'''

		if not Unit.compairable(self.type, new):
			raise CalculatorError(
				"non compairable units %s and %s." % (self.type, new))

		if self.type in Unit.base_units:
			new_amount = Unit.from_base_funcs[new](self.amount)
		elif new in Unit.base_units:
			new_amount = Unit.to_base_funcs[self.type](self.amount)
		else:
			new_amount = Unit.from_base_funcs[new](
				Unit.to_base_funcs[self.type](self.amount))

		return(Unit(float_to_str(new_amount), new))

	def convert_inplace(self, new):
		q = self.convert_to(new)
		self.amount = q.amount
		self.type = q.type

	def __floor__(self):
		return(Unit(floor(self.amount), self.type))

	def __ceil__(self):
		return(Unit(ceil(self.amount), self.type))

	def __trunc__(self):
		return(trunc(self.amount))

	def __add__(self, other):
		if isinstance(other, Unit):
			q = other.convert_to(self.type)
			q.amount += self.amount
			return(q)
		return(Unit(self.amount + other, self.type))

	def __sub__(self, other):
		if isinstance(other, Unit):
			q = other.convert_to(self.type)
			q.amount = self.amount - q.amount
			return(q)
		return(Unit(self.amount - other, self.type))

	def __radd__(self, other):
		return(other - self.amount)

	def __rsub__(self, other):
		return(other - self.amount)

	def __float__(self):
		return(float(self.amount))

	def __neg__(self):
		return(Unit(-self.amount, self.type))

	def __pos__(self):
		return(Unit(self.amount, self.type))

	def __abs__(self):
		return(Unit(abs(self.amount), self.type))

	def __round__(self, ndigits = None):
		return(Unit(round(self.amount, ndigits), self.type))

	def __mul__(self, other):
		if isinstance(other, Unit):
			return(NotImplemented)
			
			
			
		return(Unit(self.amount * other, self.type))

	def __truediv__(self, other):
		if isinstance(other, Unit):
			return(NotImplemented)
		return(Unit(self.amount / other, self.type))

	def __floordiv__(self, other):
		if isinstance(other, Unit):
			return(NotImplemented)
		return(Unit(self.amount // other, self.type))

	def __rmul__(self, other):
		if isinstance(other, Unit):
			return(NotImplemented)
		return(Unit(self.amount * other, self.type))

	def __eq__(self, other):
		if isinstance(other, Unit):
			return(
				float_to_str(self.amount)
				== float_to_str(other.convert_to(self.type)))
		return(False)

	def __lt__(self, other):
		if isinstance(other, Unit):
			return(
				float_to_str(self.amount)
				< float_to_str(other.convert_to(self.type)))
		return(False)


class NonRepeatingList(object):
	'''
	A mutable list that doesn't have two of the same element in a row.

	>>> repr(NonRepeatingList(3, 3, 4))
	'NonRepeatingList(3, 4)'
	'''

	def __init__(self, *args):
		if len(args) > 0:
			self.items = [args[0]]
			for i in args:
				if i != self.items[-1]:
					self.items.append(i)
		else:
			self.items = []

	def __getitem__(self, index):
		return(self.items[index])

	def __delitem__(self, index):
		'''
		Delete the item in the given index. If that puts two equal
		items adjacent delete the for recent one.
		'''

		del self.items[index]
		if index != 0:
			if self.items[index] == self.items[index - 1]:
				del self.items[index]

	def __contains__(self, item):
		'''
		Check if an item is in the NonRepeatingList.
		'''

		return(item in self.items)

	def __len__(self):
		return(len(self.items))

	def __repr__(self):
		return("NonRepeatingList(" + repr(self.items)[1:-1] + ")")

	def __str__(self):
		return(str(self.items))

	def __eq__(self, other):
		if isinstance(other, NonRepeatingList):
			if self.items == other.items:
				return(True)
		return(False)

	def append(self, *args):
		'''
		Add all arguments to the list if one is not the equal to the
		previous item.
		'''

		for item in args:
			if len(self.items) > 0:
				if self.items[-1] != item:
					self.items.append(item)
			else:
				self.items.append(item)

	def clear(self):
		'''
		Delete all items in the list.
		'''

		self.items.clear()


class Graph(object):
	'''
	Base class for all graphs.
	'''

	color_dict = {
		"black": (0, 0, 0),
		"red": (255, 0, 0),
		"green": (0, 128, 0),
		"blue": (0, 0, 255),
		"orange": (255, 165, 0),
		"purple": (128, 0, 128),
		"magenta": (255, 0, 255),
	}

	def __init__(
		self,
		xmin = -5, xmax = 5, ymin = -5, ymax = 5,
		wide = 400, high = 400):
		'''
		Initialize the graphing window.
		'''

		self.root = tk.Toplevel()

		self.root.title("ReCalc")

		# sets bounds
		self.xmin = xmin
		self.xmax = xmax
		self.ymin = ymin
		self.ymax = ymax

		self.xrang = self.xmax - self.xmin
		self.yrang = self.ymax - self.ymin

		# dimensions of the window
		self.wide = wide
		self.high = high

		# create the canvas
		self.screen = tk.Canvas(
			self.root,
			width = self.wide, height = self.high)
		self.screen.pack()

		self.options = tk.Menu(self.root)
		self.file_options = tk.Menu(self.options, tearoff = 0)

		self.file_options.add_command(
			label = "Save",
			command = self.save_image)
		self.file_options.add_command(
			label = "Exit",
			command = self.root.destroy)

		self.options.add_cascade(
			label = "File",
			menu = self.file_options)

		self.root.config(menu = self.options)

	def axes(self):
		'''
		Draw the axis.
		'''

		# adjusted y coordinate of x-axis
		b = self.high + (self.ymin * self.high / self.yrang)

		# adjusted x coordinate of y-axis
		a = -1 * self.xmin * self.wide / self.xrang

		try:
			# draw x-axis
			self.screen.create_line(0, b, self.wide, b, fill = "gray")

			# draw y-axis
			self.screen.create_line(a, self.high, a, 0, fill = "gray")

			self.root.update()
		except TclError as e:
			pass

	def save_image(self):
		'''
		Save the image to a file.
		'''

		fout = filedialog.asksaveasfile()
		self.image.save(fout)
		print("Saved")
