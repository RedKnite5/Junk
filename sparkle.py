import mod
# python sparkle.py


def sparkle(word):
	ln1 = " \\"
	for i in range(len(word)):
		ln1+="|"
	ln1 += "/"
	ln2 = "--" + word + "--"
	ln3 = " /"
	for i in range(len(word)):
		ln3 += "|"
	ln3 += "\\"
	print(ln1)
	print(ln2)
	print(ln3)

sparkle("sparkle")