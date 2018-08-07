from sys import argv

z, a, b, c, d = argv

print "Ok your first name is", a,
print "your middle name is", b,
print "your last name is", c,
print "and your", d,
print "Wait can you say that again."
print "What is your first name?"
print "years old."
firstname = raw_input()
print "Right. What was your middle name again?"
middlename = raw_input()
print "And your last name was?"
lastname = raw_input()
print "I remember you were", d,
print "years old"

print "Now I remember your first name is %r, your middle name is %r, and have a last name of %r." % (
	firstname, middlename, lastname)
print "Oh and don't forget you're", d,
print "years old!"
