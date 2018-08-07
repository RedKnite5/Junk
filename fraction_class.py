# fraction_class.py

class Fraction(object):
	'''A class that represents a fraction.'''
	
	def __init__(self, top, bottom):
		self.top = num
		self.bottom = bottom
	
	def __repr__(self):
		return("Fraction({top}, {bottom})".format(top=top, bottom=bottom))
	
	def __str__(self):
		return("{top}/{bottom}".format(top=top, bottom=bottom))
