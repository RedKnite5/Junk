# num_word_conversions.py



def invert_dict(d):
	new = {}
	for i in d.keys():
		new[d[i]] = i
	return new

digits = {
	"0": "zero",
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
	"10": "ten",
	"11": "eleven",
	"12": "twelve",
	"13": "thirteen",
	"14": "fourteen",
	"15": "fifteen",
	"16": "sixteen",
	"17": "seventeen",
	"18": "eighteen",
	"19": "nineteen"
}
inv_teens = invert_dict(teens)
