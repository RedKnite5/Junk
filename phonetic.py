#   phonetic.py


letters_to_pho = {"a":"alpha", "b":"bravo", "c":"charlie", "d":"delta",
"e":"echo", "f":"foxtrot", "g":"golf", "h":"hotel", "i":"india", "j":"juliett",
"k":"kilo", "l":"lima", "m":"mike", "n":"november", "o":"oscar", "p":"papa",
"q":"quebec", "r":"romeo", "s":"seirra", "t":"tango", "u":"uniform", "v":"victor",
"w":"whiskey", "x":"x-ray", "y":"yankee", "z":"zulu"}

pho_to_letters = {'alpha': 'a', 'bravo': 'b', 'charlie': 'c', 'delta': 'd',
'echo': 'e', 'foxtrot': 'f', 'golf': 'g', 'hotel': 'h', 'india': 'i',
'juliett': 'j', 'kilo': 'k', 'lima': 'l', 'mike': 'm', 'november': 'n',
'oscar': 'o', 'papa': 'p', 'quebec': 'q', 'romeo': 'r', 'seirra': 's',
'tango': 't', 'uniform': 'u', 'victor': 'v', 'whiskey': 'w', 'x-ray': 'x',
'yankee': 'y', 'zulu': 'z'}

def convert_to_phonetic(string):
	"""Convert a string or list of characters to a list of
	phonetic words. eg: alpha, bravo, charlie.
	"""

	capital_list = list((1 if x.isupper() else 0 for x in string))
	letters = list(x.lower() for x in string)
	phonetics = list(letters_to_pho[x] if x in letters_to_pho else x
	for x in letters)
	for x in range(len(phonetics)):
		if capital_list[x] == 1:
			phonetics[x] = phonetics[x].upper()
	return(phonetics)
	
def convert_to_letters(list_of_pho):
	"""Convert a list of phonetic words to a list of
	characters.
	"""

	capital_list = list((1 if x.isupper() else 0 for x in list_of_pho))
	letters = list(pho_to_letters[x.lower()] if x.lower() in pho_to_letters
	else x.lower() for x in list_of_pho)
	for x in range(len(letters)):
		if capital_list[x] == 1:
			letters[x] = letters[x].upper()
	return(letters)

s = "how are you"
print(convert_to_phonetic(s))



