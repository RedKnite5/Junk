import mymod, sys, math, itertools, re

def start():
	parse("how are you doing")

def parse(phrase0,*arg):
	if len(arg) > 0:
		sep = arg[0]
	else:
		sep = " "
	phrase = sep + phrase0.strip() + sep
	print "phrase0"
	print phrase0
	# phrase = sep + phrase0 + sep
	print "phrase"
	print phrase
	regex = sep + r"\w+" + sep
	#regex = r"\b(?=\w)" + re.escape(TEXTO) + r"\b(?!\w)"
	filter = re.compile(regex)
	matches = filter.search(phrase)
	#matches = (how, are, you, doing)
	print "filter.search(phrase)"
	print filter.search(phrase)
	print "phrase0"
	print phrase0
	print "filter.search(phrase).groups()"
	print filter.search(phrase).groups()
	print "regex"
	print regex
	print "matches"
	print matches
	print "matches.groups()"
	print matches.groups()
	print "matches.group(0)"
	print matches.group(0)
	print "matches.group(1)"
	print matches.group(1)
	print "matches.group(2)"
	print matches.group(2)
	print "matches.group(3)"
	print matches.group(3)
	

















start()














