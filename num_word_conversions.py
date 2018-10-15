# num_word_conversions.py
from math import ceil

def invert_dict(d):
	new = {}
	for i in d.keys():
		new[d[i]] = i
	return new

def values(d):
	val = []
	for i in d.keys():
		val.append(d[i])
	return val

def chunk(s, n=3):
	ans = []
	for i in range(1, ceil(len(s) / 3) + 1):
		try:
			if i != 1:
				ans.append(s[-i * n:-(i - 1) * n])
			else:
				ans.append(s[-i * n:])
		except IndexError:
			ans.append(s[:-(i - 1) * n])
	return ans[::-1]

digits = {
	"0": "",
	"1": "one",
	"2": "two",
	"3": "three",
	"4": "four",
	"5": "five",
	"6": "six",
	"7": "seven",
	"8": "eight",
	"9": "nine"
}
inv_digits = invert_dict(digits)

teens = {
	"0": "ten",
	"1": "eleven",
	"2": "twelve",
	"3": "thirteen",
	"4": "fourteen",
	"5": "fifteen",
	"6": "sixteen",
	"7": "seventeen",
	"8": "eighteen",
	"9": "nineteen"
}
inv_teens = invert_dict(teens)

tens = {
	"2": "twenty",
	"3": "thirty",
	"4": "fourty",
	"5": "fifty",
	"6": "sixty",
	"7": "seventy",
	"8": "eighty",
	"9": "ninty"
}
inv_tens = invert_dict(tens)

higher = {
	0: "",
	3: "thousand",
	6: "million",
	9: "billion",
	12: "trillion",
	15: "quadrillion",
	18: "quintillion",
	21: "sextillion",
	24: "septillion",
	27: "octillion",
	30: "nonillion",
	33: "decillion",
	36: "undecillion",
	39: "duodecillion",
	42: "tredecillion"
}


def num_2_word(num, and_in=True):
	ans = ""
	end = ""
	t = str(num)
	
	if str(num).startswith("-"):
		ans += "negative "
		start_type = type(num)
		num = start_type(t[1:])
	if "." in str(num):
		end += " point " + " ".join(map(lambda a: digits[a], list(str(num).split(".")[1])))
	
	num = int(num)
	t = str(num)
	length = len(str(num))
	r = (length - 1) // 3
	
	if length == 1:
		if t == "0":
			ans += "zero"
		ans += digits[t]
	
	elif length == 2:
		if t[0] == "1":
			ans += teens[t[1]]
		ans += f"{tens[t[0]]} {digits[t[1]]}"
	
	elif length == 3:
		ans += f"{digits[t[0]]} hundred"
		if t[1:] == "00":
			pass
		else:
			if and_in:
				ans += f" and {num_2_word(t[1:])}"
			else:
				ans += f" {num_2_word(t[1:])}"
	
	elif r > 0:
		chunks = chunk(t)[::-1]
		zipped = list(zip(chunks, values(higher)))[::-1]
		ans += " ".join(f"{num_2_word(i[0])} {i[1]}" for i in zipped if i[0] != "000")
	
	return ans + end


print(num_2_word(-.251))
