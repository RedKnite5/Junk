# Here we are getting a module
from sys import argv

# Here we are unpacking argv
script, input_file = argv

def print_all(p):
	print p.read()
	
def rewind(p):
	p.seek(0)
	
def print_a_line(line_count, p):
	print line_count, p.readline()

current_file = open(input_file)

print "First let's print the whole file:/n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)