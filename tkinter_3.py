from Tkinter import *
 


root = Tk()



w = Label(root, text="Hello Tkinter!")
w.pack()

e = Entry(root)
e.pack()

bye = ""

def sup():
	bye = e.get()
	print bye

	
textVariable = bye
f = Message(root, textVariable)
f.pack()


g = Button(root, text="press", command=sup)
g.pack()




if v == val:
	print "true"
else:
	print "not"

root.mainloop()