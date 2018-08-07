#   python coroutine_testing.py


def text(word):
	print("Looking for \"%s\"." % word)
	while True:
		line = yield
		if word in line:
			print(line)


co = text("word")
next(co)
co.send("How are you?")
co.send("Good")
co.send("fire a word")
co.close()
