#   look_and_say.py


def longest(s: str, c: str) -> int:
	'''Return the number of times c occurs at the start of s. c must be
	a single character.'''

	count = 0
	try:
		while c == s[count]:
			count += 1
	except IndexError:
		pass
	return count

def average_digits(n):
	return sum(map(int, tuple(str(n)))) / len(str(n))

def seq(seed="1"):
	yield seed
	while True:
		next = ""
		place = 0
		while place < len(seed):
			digit = seed[place]
			count = longest(seed[place:], digit)
			next += f"{count}{digit}"
			place += count
		yield next
		seed = next

look = seq()
for i in range(45):
	next(look)
print(average_digits(next(look)))
