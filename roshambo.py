import mod,random #  python roshambo.py  
while True:
	p = [("rock","paper","scissors").index(mod.lower_input("Enter your choice. (rock, paper, scissors)")),random.randint(0,2)]
	print(("rock","paper","scissors")[p[1]])
	if p[0] == p[1]: print("Tie")
	elif (p[0]+1)%3 == p[1]: print("You lose!")
	else: print("You WIN!!!")