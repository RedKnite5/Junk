# colors.py

import regex

class Color(object):
	forms = ("rgb", "hsl")
	
	def __init__(self, form, *args):
		if form not in Color.forms:
			raise ValueError("{} is not an allowed form".format(form))
		
		self.form = form
		
		if self.form == "rgb":
			self.R = int(args[0])
			self.G = int(args[1])
			self.B = int(args[2])
			self.RGB = tuple(map(int, args))
			
			self.rgb_adj = tuple(map(lambda a: a / 255, self.RGB))
			
			self.light = (max(self.rgb_adj) + min(self.rgb_adj)) / 2
			
			if self.light <= .5:
				self.sat = (max(self.rgb_adj) - min(self.rgb_adj)) /
					(max(self.rgb_adj) + min(self.rgb_adj))
			elif self.light > .5:
				self.sat = (max(self.rgb_adj) - min(self.rgb_adj)) /
					(2 - max(self.rgb_adj) - min(self.rgb_adj))
			
			if self.R >= self.G and self.R >= self.B:
				self.hue = (self.G - self.B) / 
					(self.R - min(self.RGB))
			elif self.G >= self.B and self.G >= self.R:
				self.hue = 2 + (self.B - self.R) /
					(self.G - min(self.RGB))
			elif self.B >= self.R and self.B >= self.G:
				self.hue = 4 + (self.R - self.G) /
					(self.B - min(self.RGB))
				
			self.hue = (self.hue * 60) % 360
		
		elif self.form == "hsl":
			self.hue = args[0]
			self.sat = args[1]
			self.light = args[2]
			
			if self.sat < .5:
				temp = self.light * (1 + self.sat)
			else:
				temp = self.light + self.sat - self.light * self.sat
				
			temp2 = self.light * 2 - temp
			temp_hue = self.hue / 360
			
			tempR = (temp_hue + 1/3) % 1
			tempG = temp_hue % 1
			tempB = (temp_hue - 1/3) % 1
			
			
			
			
			

white = Color("rgb", 255, 255, 255)
red = Color("rgb", 255, 0, 0)
green = Color("rgb", 0, 255, 0)





