# euler13.py

filename = "C:\\Users\\Max\\Dropbox\\Python\\50_digit_nums.txt"

with open(filename, "r") as file:
	x = sum(map(int, file.readlines()))
	print(str(x)[:10])