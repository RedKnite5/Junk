# euler89.py

filename = "C:\\Users\\Max\\Dropbox\\Python\\roman.txt"

dict = {
	"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
}

def longest(s, c):
	'''Find how many copies of c are at the begining of s.
	Assumes c is a single character.'''

	count = 1
	while True:
		if s[:count] == c*count:
			count += 1
		else:
			return(count-1)

def roman_2_int(s):
	'''Convert a Roman numeral to an int.'''
	
	total = 0
	
	if not s:
		return(0)
	if len(s) == 1:
		return(dict[s])
	start = s[0]
	

	if start in ("V", "L", "D"):
		return(roman_2_int(s[1:]) + dict[start])
	elif start == "I" and s[1] in ("V", "X"):
		return(roman_2_int(s[2:]) + dict[s[1]] - dict[start])
	elif start == "X" and s[1] in ("L", "C"):
		return(roman_2_int(s[2:]) + dict[s[1]] - dict[start])
	elif start == "C" and s[1] in ("D", "M"):
		return(roman_2_int(s[2:]) + dict[s[1]] - dict[start])
	elif start in ("I", "X", "C", "M"):
		count = longest(s, start)
		total += dict[start] * count
		return(total + roman_2_int(s[count:]))

def int_2_roman(n):
	'''Convert and integer to a Roman numeral.'''
	
	s = ""
	
	while n >= 1000:
		s += "M"
		n -= 1000
	if n >= 900:
		s += "CM"
		n -= 900
	if n >= 500:
		s += "D"
		n -= 500
	if n >= 400:
		s += "CD"
		n -= 400
	while n >= 100:
		s += "C"
		n -= 100
	if n >= 90:
		s += "XC"
		n -= 90
	if n >= 50:
		s += "L"
		n -= 50
	if n >= 40:
		s += "XL"
		n -= 40
	while n >= 10:
		s += "X"
		n -= 10
	if n == 9:
		s += "IX"
		return(s)
	if n >= 5:
		s += "V"
		n -= 5
	if n == 4:
		s += "IV"
		return(s)
	while n >= 1:
		s += "I"
		n -= 1
	return(s)

def reduce_roman(s):
	return(int_2_roman(roman_2_int(s)))


with open(filename, "r") as file:
	saved = 0
	for line in file.readlines():
		length = len(line.strip())
		s = reduce_roman(line.strip())
		#print("original: {}     new: {}".format(line, s))
		saved += length - len(s)

print(saved)

