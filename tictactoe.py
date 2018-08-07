import mod, sys

counter = 0
map = []
row = []
abc = ["A","B","C"]
for i in range(3):
	for j in range(3):
		row.append(" ")
	map.append(row)
	row = []
print("   Tic Tac Toe\n")


#map[num][let]
	
def show_board():
	print("    1   2   3")
	for i in range(3):
		print(" ","-"*13)
		print(abc[i],chr(124), map[0][i], chr(124), map[1][i], chr(124), map[2][i], chr(124))
	print(" ","-"*13)
	player()
	
def player():
	global counter
	counter += 1
	spot = mod.lower_input()
	if spot == "exit":
		sys.exit()
	if counter%2 == 1:
		piece = "X"
	else:
		piece = "O"
	letter = spot[0]
	if letter == "a":
		let = 0
	elif letter == "b":
		let = 1
	elif letter == "c":
		let = 2
	else:
		print("ERROR")
		counter-=1
		player()
	
	num = int(spot[1])-1
	
	if map[num][let] != " ":
		print("Not a valid move.")
		counter -= 1
		player()
		
	map[num][let] = piece
	output = piece + " WINS!!!"
	for i in range(3):
		if map[i][0] == map[i][1] and map[i][0] == map[i][2] and map[i][0] == ("X" or "O"):
			print(output)
			sys.exit()
	for i in range(3):
		if map[0][i] == map[1][i] and map[0][i] == map[2][i] and map[0][i] == ("X" or "O"):
			print(output)
			sys.exit()
	if map [0][0] == map[1][1] and  map[0][0] == map[2][2] and map[0][0] == ("X" or "O"):
		print(output)
		sys.exit()
	if map[0][2] == map[1][1] and map[0][2] == map[2][0] and map[0][2] == ("X" or "O"):
		print(output)
		sys.exit()
	space = 0
	for i in range(3):
		 space += map[i].count(" ")
	if space == 0:
		print("TIE")
		sys.exit()
	show_board()
	

show_board()