from math import pi,tan

def square(side):
	return(side*side)
	
def rectangle(lenght,width):
	return(lenght*width)

def circle(r):
	return(pi*r*r)

def elipse(major,minor):
	return(pi*major*minor)
	
def triangle(base,height):
	return(base*height/2)
	
def reg_polygon(side,num):
	return(num*side*side/(2*tan(180/num)))
	
def sphere(r):
	return(3*pi*r*r)
	
def cylander(r,height):
	return(2*r*r*pi+2*pi*r*height)
	
def ellipsoid(a,b,c):
	return(4*pi*(((a*b)**1.6 + (a*c)**1.6 + (b*c)**1.6)/3)**(1/1.6))
	
def torus(outer,inner):
	return((outer*outer - inner*inner)*pi*pi)
	
def rect_prism(width,length,height):
	return(width*lenght*2 + width*height*2 + lenght*height*2)
	
