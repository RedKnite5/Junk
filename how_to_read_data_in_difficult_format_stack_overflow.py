'''
SCATTER MOMENT      1

GROUP      1 FIRST      1 LAST    5
  1.000000E-00  2.000000E-00  3.000000E-00  4.000000E-00  5.000000E-00
GROUP      2 FIRST      2 LAST    5
  2.000000E-00  3.000000E-00  4.000000E-00  5.000000E-00
GROUP      3 FIRST      3 LAST    4
  3.000000E-00  4.000000E-00
GROUP      4 FIRST      4 LAST    5
  4.000000E-00  5.000000E-00
GROUP      5 FIRST      3 LAST    5
  3.000000E-00  4.000000E-00  5.000000E-00
  
SCATTER MOMENT      2
'''




def read_data(filename, start="SCATTER MOMENT      1", end="SCATTER MOMENT      2"):
	between = False
	data_next = False
	size = 0
	matrix = []
	with open(filename, "r") as file:
		for line in file.readlines():
			if start in line:
				between = True
			elif end in line:
				between = False
			elif line.startswith("GROUP"):
				data_next = True
				parts = line.split()
				first = int(parts[3])
				last = int(parts[5])
				if last > size:
					size = last
			elif data_next:
				data_next = False
				parts = line.split()
				row = [0.0] * (first-1) + list(map(float, parts))
				matrix.append(row)
	for row in matrix:
		if len(row) < size:
			row += [0.0] * (size - len(row))
	return matrix


print(read_data("hard_data.txt"))
