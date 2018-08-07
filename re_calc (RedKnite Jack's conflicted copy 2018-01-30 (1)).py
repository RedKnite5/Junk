#   python re_calc.py
#   current


import math
import statistics as stats
import sys

from pickle import load, dump
from re import compile, sub
from sympy import symbols, integrate, sympify
from sympy.solvers import  solve
from os import environ
from os.path import join

try: import tkinter as tk
except: pass


'''  To Do
	1) Deal with floating point errors
	6) complex numbers
	7) higher order derivatives
	10) graph non-functions
	11) improper integrals
	13) integrals can have non-number bounds
	14) derivatives non-number arguments
	16) absolute value with pipes
	18) set y bounds on graphs
	19) pickle degree mode
	20) graph closes only when user dictates
	21) matrices
	22) unit conversions
	23) definite integrals
	24) derivatives of functions
	25) summation
	26) big pi notation
	27) series
	28) improve tkinter interface
	29) cut off trailing zeros
	30)
'''


# changable variables
der_approx = .0001
degree_mode =  0 # 0 = off 2 = on
hist_len = 100
use_gui = True

input_widget = None
up_hist = 0
trig_func_buttons = []
inverse_trig_func_buttons = []

graph_w = 400
graph_h = 400
graph_xmin = -5
graph_xmax = 5
graph_ymin = -5
graph_ymax = 5
graph_colors = ("black","red","blue","green","orange","purple")

# multi session variables
calc_info = load(open(
join(environ["userprofile"],"dropbox\python","re_calc_info.txt"),"rb"))
history = calc_info[0]
ans = calc_info[1]

# regular expressions
if True:
	# regex for a number
	reg_num = "(-?[0-9]+\.?[0-9]*j?|-?[0-9]*\.?[0-9]+j?)"
	
	# regex for commands
	# ^$ is for an empty string
	command_reg = ("([Hh]istory)|([Qq]uit|[Ee]xit|^$)|"
	"([Dd]egree [Mm]ode)|([Rr]adian [Mm]ode)")
	command_comp = compile(command_reg)
	
	# regex for constants
	const_reg = ("(pi|π|(?<![a-z0-9])e(?![a-z0-9])|"
	"(?<!a-z)i(?![a-z])|ans(?:wer)?|tau|τ)")
	const_comp = compile(const_reg)
	
	# regex for graphing
	graph_reg = "[Gg]raph (.+)"
	graph_comp = compile(graph_reg)
	
	# regex for equation solving
	alg_reg = "[Ss]olve(.+)"
	alg_comp = compile(alg_reg)
	
	# regex for evaluating functions
	eval_reg = "[Ee]val(?:uate)? (.+?) (?:for|at) (.+)"
	eval_comp = compile(eval_reg)
	
	# regex for derivatives (must be at a number)
	der_reg = "[Dd]erivative of (.+) at "+reg_num
	der_comp = compile(der_reg)
	
	# regex for integrals (bounds must be numbers)
	int_reg = ("(?:[Ii]ntegra(?:te|l)|∫) (.+)d([a-z])"
	" (?:from )?"+reg_num+" to "+reg_num)
	int_comp = compile(int_reg)
	
	# regex for combinations and permutations
	# parentheses is to differentiate it from choose notation
	comb_reg = "(C|P)(\(.+)"
	comb_comp = compile(comb_reg)
	
	# regex for statistics functions
	ave_reg = ("([Aa]verage|[Aa]ve|[Mm]ean|[Mm]edian|[Mm]ode|"
	"[Mm]ax|[Mm]in|[Ss]tdev)(.+)")
	ave_comp = compile(ave_reg)
	
	# regex for one argument functions
	# the order does matter because of trig functions come
	# before hyperbolic functions the "h" is interpreted as
	# part of the argument for the function
	trig_reg = ("("
	"sinh|cosh|tanh|asinh|acosh|atanh|"
	"arcsinh|arccosh|arctanh|"
	"sin|cos|tan|sec|csc|cot|"
	"asin|arcsin|acos|arccos|atan|arctan|"
	"abs|ceil|floor|erf"
	")(.+)")
	trig_comp = compile(trig_reg)
	
	# regex for gamma function
	gamma_reg = "(?:[Gg]amma|Γ)(.+)"
	gamma_comp = compile(gamma_reg)
	
	# regex for logarithms
	log_reg = "[Ll]og(.+)|ln(.+)"
	log_comp = compile(log_reg)
	
	# regex for modulus
	mod2_reg = "[Mm]od(.+)"
	mod2_comp = compile(mod2_reg)
	
	# regex for parentheses
	# [^()] makes it only find the inner most parentheses
	paren_reg = "\(([^()]+)\)"
	paren_comp = compile(paren_reg)
	
	# regex for choose notation (not recursive)
	# in the form of "nCm" or "nPm"
	choos_reg = reg_num+"(C|P)"+reg_num
	choos_comp = compile(choos_reg)
	
	# ignores commas in the middle of numbers
	# could be problematic if two floats ever end up next to each other
	comma_comp = compile(reg_num+","+reg_num)
	
	# regex for exponents (not recursive)
	exp_reg = reg_num+" ?(\*\*|\^) ?"+reg_num
	exp_comp = compile(exp_reg)
	
	# regex for factorials (not recursive)
	fact_reg = reg_num+"\!"
	fact_comp = compile(fact_reg)
	
	# regex in the form x%y (not recursive)
	mod_reg = reg_num+" ?% ?"+reg_num
	mod_comp = compile(mod_reg)
	
	# regex for percentages (should probably be done without regex)
	per_reg = "%"
	per_comp = compile(per_reg)
	
	# regex for multiplication (not recursive)
	mult_reg = reg_num+" ?([*/÷]) ?"+reg_num
	mult_comp = compile(mult_reg)
	
	# regex for addition (not recursive)
	add_reg = reg_num+" ?([+-]) ?"+reg_num
	add_comp = compile(add_reg)

# list of compiled regular expressions in order
operations = [command_comp, const_comp, graph_comp,
 alg_comp, eval_comp, der_comp, int_comp,
 comb_comp, ave_comp, trig_comp, gamma_comp, log_comp, mod2_comp, paren_comp,
 # here is where the order of operations starts to matter
 # it goes: choose notation(nCm), exponents, factorial, modulus, multiplication, addition
 comma_comp, choos_comp,
 exp_comp, fact_comp, mod_comp, per_comp, mult_comp, add_comp]

#######################################################
# regular expressions not used on the immediate input #
#######################################################

# check for bounds on graph
graph_rang_reg = "(.+(?=from))(from "+reg_num+" to "+reg_num+")"
graph_rang_comp = compile(graph_rang_reg)

# check for equals sign when solving equations
eq_sides_reg = "(.+)=(.+)|(.+)"
eq_sides_comp = compile(eq_sides_reg)

# checks for specified variable when solving equations
alg_var_reg = "(.+) for ([a-z])"
alg_var_comp = compile(alg_var_reg)


def find_match(s):
	"Find matching parentheses."
	
	
	x = 0
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
	
	try: return(an,left)
	except:
		print("error ",s," is an invalad input.")
		raise ValueError

def brackets(s):
	"Inform separate whether parentheses match."
	
	x = 0
	for i in s:
		if i == "(":
			x += 1
		elif i == ")":
			x -= 1
	return(x)

def separate(s):
	"""Split up arguments of a function with commas
	like mod(x,y) or log(x,y) based on where commas that are only
	in one set of parentheses.
	"""
	
	# separate based on all commas
	terms = s.split(",")
	
	new_terms = []
	middle = False
	
	# iterate of over the groups separated by commas
	for i in range(len(terms)):
		
		# check if it is in the middle of a group of parentheses
		if middle == False:
			next_term = terms[i]
		
		# reevaluate if its in the middle of parentheses
		x = brackets(next_term)
		
		# if its not in the middle add the curren term to final list
		if x == 0:
			new_terms.append(terms[i])
			continue
		
		# if it is in the middle of a group
		if x > 0:
			
			# add the current term to the string of previous terms
			next_term = next_term + "," + terms[i+1]
			
			# check if that was the end of the group
			if brackets(next_term) == 0:
				new_terms.append(next_term)
				middle = False
			else:
				middle = True
	
	return(new_terms)


class graph(object):
	def __init__(self,
	xmin=-5,xmax=5,ymin=-5,ymax=5,
	wide=400,high=400): # all the arguments you pass the object
		
		"graphing window class"
		
		self.root = tk.Tk()
		
		# sets bounds
		self.xmin = xmin
		self.xmax = xmax
		self.ymin = ymin
		self.ymax = ymax
		
		# dimensions of the window
		self.wide = wide
		self.high = high
		
		# create the canvas
		self.screen = tk.Canvas(self.root,
		width=wide,height=high,)
		self.screen.pack()
		
		# button that close the window and program immediately
		self.close = tk.Button(self.root,text="Close",
		command=self.root.destroy)
		self.close.pack()
		
		# draws the axes
		self.axes()
	
	# method that closes window when done graphing
	def del_window(self):
		self.root.destroy()
	
	# draw the axes
	def axes(self):
		density = 500
		x = self.xmin
		xrang = self.xmax-self.xmin
		yrang = self.ymax-self.ymin
		# adjusted y coordinate of x-axis
		b = self.high + (self.ymin*self.high/yrang)
		y = 0
		slope = 0
		
		# draw x-axis
		while x < self.xmax:
			x += xrang/density
			a = (x-self.xmin)*self.wide/xrang
			self.screen.create_line(a,b,a+1,b)
		
		y = self.ymin
		# adjusted x coordinate of y-axis
		a = -1*self.xmin*self.wide/xrang
		x = 0
		
		# draw y-axis
		while y < self.ymax:
			y += yrang/density
			b = self.high - ((y-self.ymin)*self.high/yrang)
			self.screen.create_line(a,b,a+1,b)
		
		self.root.update()
	
	def xdraw(self,func,color="black"):
		density = 1000
		x = self.xmin
		xrang = self.xmax-self.xmin
		yrang = self.ymax-self.ymin
		
		while x < self.xmax:
			
			# move the x coordinate a a little
			x += xrang/density
			try:
				# eval the function at x and set that to y
				y = float(simplify("eval "+func+" at "+str(x),
				prnt=False))
				
				# find the slope at the point using the derivative
				# function of simplify
				slope = float(simplify(
				"derivative of "+func+" at "+str(x),
				prnt=False))
				
				# calculate how dense the points need to be
				# this function is somewhat arbitrary
				density = int((400*math.fabs(slope))+500)
				
				# check if the graph goes off the screen
				if y > self.ymax or y < self.ymin:
					denstiy = 2000
				
				# adjust coordinate for the screen (this is the hard part)
				a = (x-self.xmin)*self.wide/xrang
				b = self.high - ((y-self.ymin)*self.high/yrang)
				
				# draw the point
				self.screen.create_line(a,b,a+1,b,fill=color)
			except: pass
			
			# update the screen
			self.root.update()
	
	def ydraw(self,func): # not yet in use
		
		# does the same thing as xdraw but, sideways
		
		density = 1000
		y = self.ymin
		xrang = self.xmax-self.xmin
		yrang = self.ymax-self.ymin
		
		while y < self.ymax:
			y += yrang/density
			try:
				x = float(simplify("eval "+func+" at "+str(y),
				prnt=False))
				slope = float(simplify(
				"derivative of "+func+" at "+str(y),
				prnt=False))
				density = int((400*math.fabs(slope))+500)
				
				if x > self.xmax or x < self.xmin:
					denstiy = 2000
					
				a = (x-self.xmin)*self.wide/xrang
				b = self.high - ((y-self.ymin)*self.high/yrang)
				
				self.screen.create_line(a,b,a+1,b)
			except: pass
		self.root.update()


# main func
def simplify(s,prnt=True):
	"Simplify an expression."
	
	global degree_mode, graph_xmin, graph_xmax
	
	original = s
	
	# iterates over all the operations
	for i in operations:
		
		# janky solution to scientific notation being mistaken
		# for the constant e
		if i == const_comp:
			try: s = "{:.16f}".format(float(s))
			except: pass
		
		# checks for the operation
		m = i.search(s)
		
		# continues untill all instances of an operation have been dealt with
		while m != None:
			if prnt:
				print("Simplifing: ",s)
			
			#####################
			# List of Functions #
			#####################
			
			if i == command_comp:
				# non-math commands
				
				# display history
				if m.group(1) != None:
					print(history[-1*hist_len:])
				
				# exit the program
				if m.group(2) != None:
					sys.exit()
				
				# set degree mode on for the session
				if m.group(3) != None:
					degree_mode = 2
				
				# set degree mode off for the session
				if m.group(4) != None:
					degree_mode = 0
				
				return(1)
			
			if i == const_comp:
				
				# program variables and mathematical constants
				
				if prnt:
					print("Replacing constants")
					
				# pi
				if m.group(1) in ("pi","π"):
					result = math.pi
				
				# e
				elif m.group(1) == "e":
					result = math.e
				
				# i (this doesn't really work yet)
				elif m.group(1) == "i":
					result = 1j
				
				# the output of the previous query
				elif m.group(1) in ("ans","answer"):
					result = ans
				
				# tau (equivalent to 2*pi)
				elif m.group(1) in ("tau","τ"):
					result = math.tau
				
				# should never happen debugging use only
				else:
					print(m.group(0))
			
			if i == graph_comp:
				
				# looks for x bounds on the graph
				range_m = graph_rang_comp.search(m.group(1))
				if range_m != None:
					m = range_m	
				
				# checks to see if tkinter is installed to graph things at all
				if "tkinter" in sys.modules:
						
					if prnt:
						print("Graphing")
					
					# finds multiple functions to graph
					funcs_to_graph = m.group(1).split(" and ")
					
					# sets bounds to bounds given
					if range_m != None:
						graph_xmin = float(m.group(3))
						graph_xmax = float(m.group(4))
					
					# informs the user of the x bounds
					if prnt:
						print("range",graph_xmin,graph_xmax)
					
					# creates graph object
					made_graph = graph(
					xmin=graph_xmin,xmax=graph_xmax,
					ymin=graph_ymin,ymax=graph_ymax,
					wide=graph_w,high=graph_h)
					
					# works out how many times it needs to loop the colors its using
					color_loops = math.ceil(len(funcs_to_graph)/len(graph_colors))
					
					# passes functions to be graphed and the color to do so with
					for f, c in zip(funcs_to_graph,graph_colors*color_loops):
						made_graph.xdraw(f,color=c)
					
					# closes the graphing window
					made_graph.del_window()
				
				# informs the user of reason for failure
				else: print("Could not graph. tkinter is not installed")
				return(1)
			
			if i == alg_comp:
				
				# solve equations using sympy. If there is no equals
				# sign it is assumed the expression equals zero
				
				if prnt:
					print("Solving equations")
				
				# find if there is a specified variable
				varm = alg_var_comp.search(m.group(1))
				
				# find the variable its solving for. defaults to "x"
				if varm == None:
					x = symbols("x")
					eq = m.group(1)
				else:
					x = symbols(varm.group(2)[-1])
					eq = varm.group(1)
				
				# if there is an equals sign solve for zero and use sympy
				# to solve it
				em = eq_sides_comp.search(eq)
				if em.group(3) == None:
					sym_zero = sympify(em.group(1) + "-(" + em.group(2) + ")")
					temp_result = solve(sym_zero,x)
					
					# if there is only one result make it the result
					# otherwise return the list
					if len(temp_result) == 1:
						result = temp_result[0]
					else:
						result = temp_result
				
				# if there isn't an equals sign use sympy to solve
				else:
					temp_result = solve(em.group(3),x)
					
					# if there is only one result make it the result
					# otherwise return the list
					if len(temp_result) == 1:
						result = temp_result[0]
					else:
						result = temp_result
			
			if i == eval_comp:
				
				# evaluations are done by substituting x for the number you
				# want to evaluate at
				# functions must be in terms of x
				
				if prnt:
					print("Evaluating functions")
				
				# substituting the point for x in the function and evaluating 
				# that recursively
				result = simplify(sub("(?<![a-z])x",
				m.group(2),m.group(1)),prnt=prnt)
			
			if i == der_comp:
				
				# derivatives are calculated by evaluating
				# the slope between two points on either side of the point
				# you are trying to find the slope of
				
				if prnt:
					print("Differentiating")
				
				# find the point on either side of the desired point
				x_one = float(m.group(2))+der_approx
				x_two = float(m.group(2))-der_approx
				
				# find the change in y value between the two points
				delta_y = float(simplify("eval "+m.group(1)+" for "+
				str(x_one),prnt=prnt))-float(simplify("eval "+m.group(1)+" for "+
				str(x_two),prnt=prnt))
				
				# divide by the length of the interval to find the slope
				result = delta_y/(2*der_approx)
			
			if i == int_comp:
				
				# Integrals are done with sympy
				# Integrals must be in a form that sympy can integrate
				# The bounds must be numbers not expressions
				# The integral must have a "dx" or whatever variable you are using
				
				if prnt:
					print("Integrating")
				
				# using sympy to integrate
				result = integrate(m.group(1),
				(m.group(2),m.group(3),m.group(4)))
			
			if i in (comb_comp, choos_comp):
				
				# combinations and permutations written
				# both as C(5,2) and 5C2 evaluated as: 5 choose 2
				# if written as mCn it will only take numbers not expressions
				# unless parentheses are used. In order of operations nCm comes first.
				# Combinations and permutations both used the gamma function
				# in place of factorials and as a result will take
				# non-integer arguments
				
				if i == choos_comp: # if written as nCm
					
					# turn the arguments into floats and give them more
					# descriptive names
					inner_n = float(m.group(1))
					inner_m = float(m.group(3))
					
					if prnt:
						if m.group(2) == "C":
							print("Doing combinations")
						else:
							print("Doing permutations")
					
					# find permutations
					result = math.gamma(1+inner_n)/math.gamma(1+inner_n-inner_m)
					
					# if combinations also divide by m!
					if m.group(2) == "C":
						result = result/math.gamma(1+inner_m)
				
				else: # if written as C(5,2)
					
					# find the arguments of the function and cut off
					# everything else
					# sin(C(5,2)) ← the last parenthesis
					proto_inner = find_match(m.group(2))
					
					# remove outer parentheses
					x = proto_inner[0][1:-1]
					
					# separate the arguments
					comb_args = separate(x)
					
					# evaluate each of the arguments separately
					inner_n = float(simplify(comb_args[0],prnt=prnt))
					inner_m = float(simplify(comb_args[1],prnt=prnt))
					
					
					if prnt:
						if m.group(1) == "C":
							print("Doing combinations")
						else:
							print("Doing permutations")
					
					# find permutations
					result = math.gamma(1+inner_n)/math.gamma(1+inner_n-inner_m)
					
					# if combinations also divide by m!
					if m.group(1) == "C":
						result = result/math.gamma(1+inner_m)
					
					# add on anything that was was cut off the end when finding
					# the arguments
					# sin(C(5,2)) ← the last parenthesis
					result = str(result) + proto_inner[1]
			
			if i == ave_comp:
				
				# general statistics functions 
				# this may in the future include any function that
				# can have an arbitrarily large number of arguments
				
				if prnt:
					print("Averaging")
				
				# find the arguments of the function and cut off
				# everything else
				# sin(mean(4,2)) ← the last parenthesis
				proto_inner = find_match(m.group(2))
				
				# separate the arguments based on commas that are not
				# within more than one set of parentheses
				ave_args = separate(proto_inner[0][1:-1])
				
				# evaluate all the arguments
				list_ave = list(map((lambda x: float(simplify(x))),ave_args))
				
				# perform the different functions
				if m.group(1).lower() in ("ave","average","mean"):
					result = stats.mean(list_ave)
				if m.group(1).lower() == "median":
					result = stats.median(list_ave)
				if m.group(1).lower() == "mode":
					result = stats.mode(list_ave)
				if m.group(1).lower() == "max":
					result = max(list_ave)
				if m.group(1).lower() == "min":
					result = min(list_ave)
				if m.group(1).lower() in ("stdev"):
					result = stats.stdev(list_ave)
				
				# add on anything that was was cut off the end when finding
				# the arguments
				# sin(mean(4,2)) ← the last parenthesis
				result = str(result)+proto_inner[1]				
				
			if i == trig_comp:
				
				# let the user know what opperation the program is doing
				if prnt:
					if m.group(1) not in ("abs","ceil","floor","erf"):
						print("Doing trigonometry")
					
					elif m.group(1) == "abs":
						print("Finding absolute value")
					
					elif m.group(1) in ("ceil","floor"):
						print("Rounding")
					
					elif m.group(1) == "erf":
						# refers to the Gaussian error function
						print("Using error function")
				
					# find the arguments of the function and cut off
					# everything else
					# tan(sin(π)) ← the last parenthesis when 
					# evaluating sin
				proto_inner = find_match(m.group(2))
				
				# looks for the degree symbol in the argument 
				# if the program finds it degree mode is set to true
				# for the particular operation
				if "°" in proto_inner[0] and degree_mode == 0:
					degree_mode = 1
					proto_inner[0] = sub("[°]","",proto_inner[0])
					
				# evaluate the argument into a form that math.log
				# can accept
				inner = float(simplify(proto_inner[0],prnt=prnt))
				
				# check if in degree mode and if its doing an
				# operation that takes an angle as an argument
				if degree_mode > 0:
					if m.group(1) in ("sin","sec",
					"cos","csc","tan","cot",
					"sinh","cosh","tanh"):
						inner = math.pi*inner/180
				
				# trig functions and inverse trig functions
				if m.group(1) == "sin":
					result = math.sin(inner)
				if m.group(1) == "cos":
					result = math.cos(inner)
				if m.group(1) == "tan":
					result = math.tan(inner)
				if m.group(1) == "sec":
					result = 1/math.cos(inner)
				if m.group(1) == "csc":
					result = 1/math.sin(inner)
				if m.group(1) == "cot":
					result = 1/math.tan(inner)
				if m.group(1) in ("asin","arcsin"):
					result = math.asin(inner)
				if m.group(1) in ("acos","arccos"):
					result = math.acos(inner)
				if m.group(1) in ("atan","arctan"):
					result = math.atan(inner)
				
				# hyperbolic functions and inverse hyperbolic functions
				if m.group(1) == "sinh":
					result = math.sinh(inner)
				if m.group(1) == "cosh":
					result = math.cosh(inner)
				if m.group(1) == "tanh":
					result = math.tanh(inner)
				if m.group(1) in ("asinh","arcsinh"):
					result = math.asinh(inner)
				if m.group(1) in ("acosh","arccosh"):
					result = math.acosh(inner)
				if m.group(1) in ("atanh","arctanh"):
					result = math.atanh(inner)
				
				# other single argument functions
				if m.group(1) == "abs":
					result = math.fabs(inner)
				if m.group(1) == "ceil":
					result = math.ceil(inner)
				if m.group(1) == "floor":
					result = math.floor(inner)
				if m.group(1) == "erf":
					result = math.erf(inner)
				
				# checks if its in degree mode (not because of
				# degree symbols in the argument) and if so
				# converts the answer to degrees for functions that
				# output an angle
				if m.group(1) in ("asin",
				"arcsin","acos","arccos","atan","arctan",
				"asinh","arcsinh","acosh","arccosh",
				"atanh","arctanh") and degree_mode == 2:
					result = result*180/math.pi
				
				# resets the degree mode for the session
				if degree_mode == 1:
					degree_mode = 0
				
				# this is a jankey fix for the output being in
				# scientific notation and the program mistaking the
				# e for the constant e
				try: result = "{:.16f}".format(float(result))
				except: pass
				
				# add back anything that was cut off when finding the
				# argument of the inner function
				# tan(sin(π)) ← the last parenthesis when 
				# evaluating sin
				result = str(result)+proto_inner[1]
			
			if i in (gamma_comp, fact_comp):
				
				# factorials and the gamma function
				# interprets x! mathematically as gamma(x+1)
				# if written with an "!" will only take numbers as an argument.
				# In order of operations factorials come after exponents,
				# but before modulus
				
				if i == gamma_comp: # the user inputed the gamma function
					
					if prnt:
						print("Doing the gamma function")
					
					# find the arguments of the function and cut off
					# everything else
					# sin(gamma(5)) ← the last parenthesis
					proto_inner = find_match(m.group(1))
					
					# evaluating the argument
					inner = float(simplify(proto_inner[0],prnt=prnt))
					
					# doing the calculation
					result = math.gamma(inner)
					
					# add back anything that was cut off when finding the
					# argument of the inner function
					# sin(gamma(5)) ← the last parenthesis
					result = str(result)+proto_inner[1]
				
				if i == fact_comp: # the user inputed a factorial
					
					if prnt:
						print("Doing factorials")
					
					# evaluating the argument
					inner = float(simplify(str(float(m.group(1))+1),prnt=prnt))
					
					# doing the calculation
					result = math.gamma(inner)
			
			if i == log_comp:
				
				# logarithms written as log(x,y) where y
				# is the base and written as ln(x)
				
				if prnt:
					print("Doing logarithms")
				
				if m.group(1) != None: # if written as log(x,y)
					
					# find the arguments of the function and cut off
					# everything else
					# sin(log(4,2)) ← the last parenthesis 
					proto_inner = find_match(m.group(1))
					
					# separate the arguments based on commas that are not
					# within more than one set of parentheses
					log_args = separate(proto_inner[0][1:-1])
					
					# evaluate the arguments individually into a form that math.log
					# can accept
					inner1 = float(simplify(log_args[0],prnt=prnt))
					inner2 = float(simplify(log_args[1],prnt=prnt))
					
					# perform the logarithm
					result = math.log(inner1,inner2)
				
				
				elif m.group(2) != None: # if written as ln(x)
					
					# find the argument of the function and cut off
					# everything else
					# sin(ln(e)) ← the last parenthesis 
					proto_inner = find_match(m.group(2))
					
					# perform the logarithm
					result = math.log(float(simplify(proto_inner[0],prnt=prnt)))
				
					# add on anything that was was cut off the end when finding
					# the arguments
					# sin(log(4,2)) ← the last parenthesis
				result = str(result) + proto_inner[1]
			
			if i == paren_comp:
				
				# recursively evaluates the innermost parentheses
				
				if prnt:
					print("Looking at parentheses")
				result = simplify(m.group(1),prnt=prnt)
			
			if i == comma_comp:
				
				# just concatenates whats on either side
				# of the parentheses unless its separating
				# arguments of a function
				
				result = float(m.group(1)+m.group(2))
			
			if i == exp_comp:
				
				# exponents
				
				if prnt:
					print("Doing exponents")
				
				result = float(m.group(1))**float(m.group(3))
			
			if i in (mod_comp, mod2_comp):
				
				# modulus written as both mod(x,y) and x%y 
				# where x is the dividend and y is the divisor
				# if written as x%y it will only take numbers for arguments.
				# In order of operations modulus comes after exponents and
				# factorials, but before multiplication and division
				
				if prnt:
					print("Doing modulus")
				if i == mod2_comp:
					
					# find the arguments of the function and cut off
					# everything else
					# sin(mod(5,2)) ← the last parenthesis
					proto_inner = find_match(m.group(1))
					
					# separate the arguments based on commas that are not
					# within more than one set of parentheses
					mod_args = separate(proto_inner[0][1:-1])
					
					# evaluate the arguments individually into a form that fmod
					# can accept
					inner1 = float(simplify(mod_args[0],prnt=prnt))
					inner2 = float(simplify(mod_args[1],prnt=prnt))
					
					# do the actual modulation
					result = math.fmod(inner1,inner2)
					
					# add on anything that was was cut off the end when finding
					# the arguments
					# sin(mod(5,2)) ← the last parenthesis
					result = str(result)+proto_inner[1]
				else:
					
					# the x%y format
					result = math.fmod(float(m.group(1)),float(m.group(2)))
			
			if i == per_comp:
				
				# percentage signs act just like dividing by 100
				
				if prnt:
					print("Converting percentages")
				result = "/100"
			
			if i == mult_comp:
			
				# multiplication and division
				
				if m.group(2) == "*":
					if prnt:
						print("Multiplying")
					result = float(m.group(1))*float(m.group(3))
				if m.group(2) in ("/","÷"):
					if prnt:
						print("Dividing")
					result = float(m.group(1))/float(m.group(3))
			
			if i == add_comp:
				
				# addition and subtraction
				
				if m.group(2) == "+":
					if prnt:
						print("Adding")
					result = math.fsum((float(m.group(1)),float(m.group(3))))
				if m.group(2) == "-":
					if prnt:
						print("Subtracting")
					result = float(m.group(1))-float(m.group(3))
			
			if i not in (command_comp, const_comp,
			alg_comp, eval_comp, der_comp):
				
				# this is a jankey fix for python returning answers in
				# scientific notation which since it has e it mistakes
				# the constant e
				
				try: result = "{:.16f}".format(result)
				except: pass
			
			# replace the text matched by i: the regular expression
			# with the result of the mathematical expression
			s = sub(i,str(result),s,count=1)
			m = i.search(s)
	try: s = "{:.16f}".format(s)
	except:
		if s == original and prnt:
			print(s," is not a number and was not operated on")
			raise ValueError
	return(s)


# pre and post processing for console
def ask(s=None):
	"""Ask the user what expression they want to simplify
	and do pre and post processing
	"""
	
	global ans
	if s == None:
		
		# get input from the user
		s = input("input an expression: ")
		
		# add the user input to the history
		history.append(s)
		
		# save history to file
		calc_info = [history,ans]
		dump(calc_info,open(join(
		environ["userprofile"],"dropbox\python","re_calc_info.txt"),"wb"))
	
	# evaluate the expression
	out = simplify(s)
	
	# save output to be used by the user
	ans = out
	
	# display the output
	print(out)
	print("Done")
	print("")
	
	# save answer to file to be used next session
	calc_info = [history,ans]
	dump(calc_info,open(join(
	environ["userprofile"],"dropbox\python","re_calc_info.txt"),"wb"))


def key_pressed(event):
	
	global up_hist
	
	try: code = event.keycode
	except: code = event
	print(code)
	
	if code == 13: # enter
		get_input()
	
	if code == 38: # up arrow
		up_hist += 1
		input_widget.delete(0, "end")
		input_widget.insert(0, history[-1*up_hist])
		
	if code == 40: # down arrow
		if up_hist > 1:
			up_hist -= 1
			input_widget.delete(0, "end")
			input_widget.insert(0, history[-1*up_hist])
	
	if code not in (38,40):
		up_hist = 0

def input_backspace():
	"Delete the last character in the entry widget."
	
	global input_widget
	
	a = input_widget.get()
	input_widget.delete(0, "end")
	input_widget.insert(0, a[:-1])

def get_input():
	"Get user input from the entry widget."
	
	global ans, mess
	
	s = input_widget.get()
	
	# add the user input to the history
	history.append(s)
	
	# save history to file
	calc_info = [history,ans]
	dump(calc_info,open(join(
	environ["userprofile"],"dropbox\python","re_calc_info.txt"),"wb"))
	
	out = simplify(s,prnt=False)
	
	# save output to be used by the user
	ans = out
	
	# display the output
	mess.set(out)
	
	# save answer to file to be used next session
	calc_info = [history,ans]
	dump(calc_info,open(join(
	environ["userprofile"],"dropbox\python","re_calc_info.txt"),"wb"))
	
	input_widget.delete(0, "end")

def switch_trig():
	"Use grid on the trig function buttons."
	print("working")
	trig_func_buttons[0].grid(row=3, column=7)
	trig_func_buttons[1].grid(row=3, column=8)
	trig_func_buttons[2].grid(row=3, column=9)
	
	
def switch_inverse_trig():
	"Use gird on the inverse trig function buttons."
	
	

def tkask(s=None):
	"Make a GUI for the program"
	
	global input_widget, mess, trig_func_buttons, inverse_trig_func_buttons
	
	root = tk.Tk()
	
	mess = tk.StringVar()
	mess.set("Input an expression")
	
	output_mess_widget = tk.Message(root,textvariable=mess,width=200)
	output_mess_widget.grid(row=0, column=0, columnspan=20)
	
	input_widget = tk.Entry(root,width=90)
	input_widget.grid(row=1, column=0, columnspan=20)
	
	button_keys = list(range(10))+[".","+","-","*","÷","^","!"]
	
	digit_button = list(tk.Button(root,text=str(i),
	command=lambda k=i: input_widget.insert("end",k),width=5) for i in button_keys)
	
	digit_button[7].grid(row=3, column=0)
	digit_button[8].grid(row=3, column=1)
	digit_button[9].grid(row=3, column=2)
	
	digit_button[4].grid(row=4, column=0)
	digit_button[5].grid(row=4, column=1)
	digit_button[6].grid(row=4, column=2)
	
	digit_button[1].grid(row=5, column=0)
	digit_button[2].grid(row=5, column=1)
	digit_button[3].grid(row=5, column=2)
	
	digit_button[0].grid(row=6, column=0)
	digit_button[10].grid(row=6, column=1) # .
	
	digit_button[11].grid(row=3, column=4) # +
	digit_button[12].grid(row=3, column=5) # -
	digit_button[13].grid(row=4, column=4) # *
	digit_button[14].grid(row=4, column=5) # ÷
	digit_button[15].grid(row=5, column=4) # ^
	digit_button[16].grid(row=5, column=5) # !
	
	equals_button = tk.Button(root, text="=",
	command=get_input, width=5, bg="blue")
	
	back_button = tk.Button(root, text="delete",
	command=input_backspace, width=5)
	
	equals_button.grid(row=6, column=2)
	back_button.grid(row=3, column=19)
	
	trig_funcs = ("sin(","cos(","tan(","sec(","csc(","cot(")
	
	trig_func_buttons = list(tk.Button(root,text=i[:-1],
	command=lambda k=i: input_widget.insert("end",k),
	width=5) for i in trig_funcs)
	
	inverse_trig_funcs = ("arcsin(","arccos(","arctan(","arcsec(","arccsc(","arccot(")
	
	inverse_trig_func_buttons = list(tk.Button(root,text=i[:-1],
	command=lambda k=i: input_widget.insert("end",k),
	width=5) for i in inverse_trig_funcs)
	
	
	menubar = tk.Menubutton(root, text="Functions", relief="raised")
	dropdown = tk.Menu(menubar, tearoff=0)
	dropdown.add_command(label="Trig Functions", command=switch_trig)
	dropdown.add_command(label="Inverse Trig Functions", command=switch_inverse_trig)
	
	menubar.config(menu=dropdown)
	
	menubar.grid(row=3, column=18)
	
	
	root.bind("<Key>",key_pressed)
	
	root.mainloop()
	
	



# handling command line arguments and startup
if len(sys.argv) == 1:
	if "tkinter" in sys.modules and use_gui:
		tkask()
	else:
		while True: ask()
	
else:
	history.append(" ".join(sys.argv[1:]))
	
	if "tkinter" in sys.modules and use_gui:
		tkask(" ".join(sys.argv[1:]))
	else:
		ask(" ".join(sys.argv[1:]))

# main loop
if "tkinter" in sys.modules and use_gui:
	pass
else:
	while True: ask()

