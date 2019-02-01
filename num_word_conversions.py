# num_word_conversions.py
from math import ceil
import re


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


def replace(l, d):
	ans = []
	for i, v in enumerate(l):
		try:
			ans.append(d[v])
		except KeyError:
			ans.append(l[i])
	return ans


def is_num(n):
	try:
		int(n)
		return True
	except ValueError:
		return False


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
	42: "tredecillion",
	45: "quattuordecillion",
	48: "quindecillion",
	51: "sexdecillion",
	54: "septemdecillion",
	57: "octodecillion",
	60: "novemdecillion",
	63: "vigintillion",
	66: "unvigintillion",
	69: "duovigintillion",
	72: "trevigintillion",
	75: "quattuorvigintillion",
	78: "quinvigintillion",
	81: "sexvigintillion",
	84: "septvigintillion",
	87: "octovigintillion",
	90: "nonvigintillion",
	93: "trigintillion",
	96: "untrigintillion",
	99: "duotrigintillion"
}
inv_higher = invert_dict(higher)


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
	
	if length > 101:
		raise ValueError("Can not accept inputs larger that 10^101")
	
	if length == 1:
		if t == "0":
			ans += "zero"
		else:
			ans += digits[t]
	
	elif length == 2:
		if t[0] == "1":
			ans += teens[t[1]]
		else:
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


def text_2_num(text):
	text = text.lower()
	words = re.split(r"\W+", text)
	words_digits = replace(words, inv_digits)
	print(words_digits)
	
	number = []
	for i in words_digits:
		if i == "hundred":
			number[-1] = int(number[-1]) * 100
		elif i in inv_teens:
			number.append(10 + int(inv_teens[i]))
		elif i in inv_tens:
			number.append(int(inv_tens[i]) * 10)
		elif i in higher:
			number.append(10 ** int(inv_higher[i]))
		else:
			number.append(i)
	
	result = [0]
	for i in number:
		try:
			result[-1] += int(i)
		except ValueError:
			if i == "and":
				continue
			else:
				result.append(i)
				result.append(0)
				continue
	print(result)


if __name__ == "__main__":
	print(text_2_num("three hundred and twenty three thousand two hundred and ten"))
