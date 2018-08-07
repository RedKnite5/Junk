# euler59.py

from string import ascii_lowercase as letters
from itertools import cycle

filename = "C:\\Users\\Max\\Dropbox\\Python\\cipher.txt"


def three_letter_codes():
	'''Generate every possible three letter code.'''
	
	for a in letters:
		for b in letters:
			for c in letters:
				yield (ord(a), ord(b), ord(c))


with open(filename, "r") as file:
	line = file.readlines()[0]
	
	codes = line.split(",")
	
	for i in three_letter_codes():
		decrypted_codes = [chr(int(c) ^ k) for c, k in zip(codes, cycle(i))]
		
		decrypted = "".join(decrypted_codes)
		
		if any(a in decrypted for a in ("number", "text", "letter", "word", "answer", "the", "and")) and all(a not in decrypted for a in "@#%^&$}{"):
			print(decrypted)
			print(sum(map(ord, decrypted_codes)))
			break
