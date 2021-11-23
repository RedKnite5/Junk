import math as m
import sys

"""
cd documents
cd python
python calculator.py
"""



def start(x_factor_1, area):
	del potential_factors[:]
	del factors[:]
	del divisors[:]
	del new_poly[:]
	del poly_factors[:]
	del sides[:]
	del angles[:]
	x_factor_1 = 0
	print " "
	print " "
	print "starting..."
	del poly_factors[:]
	stuff = raw_input()
	selection = stuff.lower()
	if selection == "factor poly" or selection == "factor polynomial":
		get_poly(x_factor_1)
	elif selection == "triangle":
		get_tri_info(area)
	elif selection == "exit" or selection == "quit":
		print "bye"
		sys.exit()
	else:
		print "ERROR"
	

def factor(number):
	for x in range(1,int(m.ceil(m.pow(abs(float(number)),.5))+1)):
		potential_factors.append(x)
	for x in potential_factors:
		divisable =  number % potential_factors[x-1] == 0
		if divisable:
			factors.append(x)
			factors.append(number/x)
	print factors
	if factors[len(factors)-1] == factors[len(factors)-2]:
		factors.pop()
	answer=[]
	for x in range(len(factors)):
		answer.append(factors[x])
	del factors[:]
	del potential_factors[:]
	return answer
	
def get_poly(x_factor_2):
	print "degree of polynomial"
	degree = input()+1
	for x in range(0,degree):
		print "coefficent #",x+1,":"
		coefficent = raw_input()
		poly.append(coefficent)
	factor_poly(x_factor_2)
		
def factor_poly(x_factor_3):
	constant = int(poly[len(poly)-1])
	leading_coefficent = int(poly[0])
	
	if constant == 0:
		x_factor_3 += 1
		poly.pop()
		factor_poly(x_factor_3)
		
	factors_p = factor(constant)
	factors_q = factor(leading_coefficent)

	for p in factors_p:
		for q in factors_q:
			for x in range(0,2):
				d = (m.pow((-1),x)*p)/q
				if divisors.count(d)==0:
					divisors.append(d)

	for x in divisors:
		new_poly.append(float(poly[0]))
		for y in range(len(poly)-1):
			
			new_poly.append((float(new_poly[y])*x)+float(poly[y+1]))
		if new_poly[len(new_poly)-1] ==0:
			print "this is a success"
			poly_factors.append(x*-1)
			print x
			del poly[:]
			for v in range(len(new_poly)):
				poly.append(new_poly[v])
			poly.pop()
			del potential_factors[:]
			del factors[:]
			del divisors[:]
			del new_poly[:]
			
			factor_poly(x_factor_3)
		del new_poly[:]
	give_factored_answer(x_factor_3)
	

def give_factored_answer(x_factor_4):
	for x in range(x_factor_4):
		print "x"
	for x in range(len(poly_factors)):
		if poly_factors[x] > 0:
			print "(x+%d)" %float(poly_factors[x])
		else:
			print "(x%d)" %float(poly_factors[x])
	if len(poly) != 1 or poly[0] != 1.0:
		print poly
	start(x_factor_4)
	
def get_tri_info(area):
	print ""
	print "If you don't know something just type \"idk\""
	print "How many sides do you know?"
	num_sides = raw_input()
	if num_sides == "0" or num_sides == "1" or num_sides == "2":
		print "How many angles do you know?"
		num_angles = input()
		if num_angles != 0:
			for a in range(len(letters)):
				print "What is angle %s?" %letters[a]
				angle = raw_input()
				angles.append(angle)
				print angles
		print "Do you know the area?"
		area_know = raw_input()
		if area_know.lower() == "yes":
			print "What is it?"
			area = input()
	elif num_sides =="3":		
		"""do stuff"""
	else:
		print "ERROR"
		del num_sides
		get_tri_info()
	if num_sides !=0:
		for l in range(len(letters)):
			print "What is side %s?" %letters[l]
			side = raw_input()
			sides.append(side)
			print sides
	solve_triangle(area, area_know)
		
def solve_triangle(area, area_know):
	if sides.count("idk") == 0:
		f_tri_angles()
		s = (float(sides[0])+float(sides[1])+float(sides[2]))/2
		area = pow(s*(s-sides[0])*(s-sides[1])*(s-sides[2]),.5)
		give_triangle_answer(area)
	if sides.count("idk") == 1 and area_know.lower() == "yes":
		f_side_with_area(area)
	
	
def f_tri_angles():
	for x in range(3):
		angles.append(m.acos((m.pow(sides[(x+1)%3],2)+m.pow(sides[(x+2)%3],2)-m.pow(sides[(x)%3],2))/(2*sides[(x+1)%3]*sides[(x+2)%3])))
	
def f_tri_area():
	s = (sides[0]+sides[1]+sides[2])/2
	area = m.pow(s*(s-sides[0])*(s-sides[1])*(s-sides[2]),.5)
	
def f_side_with_area(area):
	for x in range(3):
		if sides[x] != "idk":
			known_sides.append(float(sides[x]))
	herons_poly.append(-1*(m.pow((known_sides[0]+known_sides[1]),2)+m.pow((known_sides[0]-known_sides[1]),2)))
	herons_poly.append((16*area*area)-(m.pow((known_sides[0]+known_sides[1]),2)*m.pow((known_sides[0]-known_sides[1]),2)))
	print herons_poly
	quad_form(herons_poly[0],herons_poly[1],herons_poly[2])
	print m.pow(quad_form_ans[0],.5)
	print m.pow(quad_form_ans[1],.5)
	
	
	
def give_triangle_answer(area_1):
	for x in range(3):
		print "Side %s: %f" %(letters[x], sides[x])
	for x in range(3):
		print "Angle %s: %f" %(letters[x], m.degrees(angles[x]))
	print "Area: %f" %area_1
	
	
	start(x_factors, area_1)
	
	
def quad_form(quad_a, quad_b, quad_c):
	quad_form_ans.append(-1*quad_b+(m.pow(m.pow(quad_b,2) - 4*quad_a*quad_c,.5)))
	quad_form_ans.append(-1*quad_b-(m.pow(m.pow(quad_b,2) - 4*quad_a*quad_c,.5)))
	return quad_form_ans
		

	

letters = ['a', 'b', 'c']
sides = []
angles = []
herons_poly = [1.0]
known_sides = []
potential_factors = []
factors = []	
poly = []
new_poly = []
divisors = []
poly_factors = []
quad_form_ans = []

x_factors = 0
area = 0
	
start(x_factors, area)
