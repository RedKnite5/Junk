# png_format.py

import binascii

def make_png(data):
	with open("png_test.png") as file:
		file.write(binascii.unhexlify("".join(data)))

def make_data():
	data = []
	header = ["89", "50", "4E", "47"]
	data += header
	
	