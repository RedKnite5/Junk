from Tkinter import *

master = Tk()

def callback():
    print "click!"

b = Button(Tk(), text="OK", command=callback)
b.pack()

mainloop()