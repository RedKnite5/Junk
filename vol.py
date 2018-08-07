from math import pi

def sphere(r):
	return((4/3)*pi*r*r*r)
	
def cylendar(r,height):
	return(pi*r*r*height)
	
def cone(r,height):
	return(pi*r*r*height/3)
	
def rectangular_prism(width,depth,height):
	return(width*depth*height)
	
def cube(side):
	return(side*side*side)
	
def ellipsoid(a_axis,b_axis,c_axis):
	return((4/3)*pi*a_axis*b_axis*c_axis)
	
def rectangular_pyramid(width,depth,height):
	return(width*depth*height/3)
	
def prism(area,height):
	return(area*height)
	
def pyramid(area,height):
	return(area*height/3)
	
def tetrahedron(side):
	return(side*side*side*(2**.5)/12)
	
def octahedron(side):
	return(side*side*side*(2**.5)/3)
	
def dodecahedron(side):
	return(side*side*side*((5**.5)*7+15)/4)

def icosahedron(side):
	return(side*side*side*((15+(5**.5)*5)/12))
	
def torus(big_rad,small_rad):
	return(2*pi*pi*big_rad*small_rad*small_rad)