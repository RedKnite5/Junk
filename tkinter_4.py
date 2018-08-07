i = 0

from Tkinter import *
import mymod, sys

root = Tk()


"""
e = Entry(root)
e.pack()
"""



def output(output):
	m = Message(root, text=output, width=400, font=(12))
	m.pack()
	
def calculator():
	if i == 0:
		print "First number"
		num_1 = input()
	elif i == 1:
		print "Second number"
		num_2 = input()
	elif i == 2:
		answer = float(num_1) + float(num_2)
		output(answer)
	else:
		print "ERROR"
		sys.exit()
		
	return
	

	
b = Button(root, text="Enter", command=calculator)
b.pack()


	

	
	
root.mainloop()