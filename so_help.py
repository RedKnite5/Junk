rows = int(input("ENTER NUMBER OF ROWS: "))
x = 0
count = 0
z =0
for i in range (rows, 0 , -1):
	print(" "*i , end ="")
	x += 1
	print("*" * x, end ="")
	count += 1
	if count == 1:
		print("")
	if count>1:
		z += 1
		print("*" * z)