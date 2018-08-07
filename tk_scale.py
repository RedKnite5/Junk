import mod
import tkinter as tk
# python testing.py

root = tk.Tk()

def b1(): print(scale.get())
def b2(): print("no")

yes = tk.Button(root,text="yes",command=b1)
yes.pack(side="right")

no = tk.Button(root,text="no",command=b2)
no.pack(side="right")

scale = tk.Scale(root,from_=0,to=100,orient="horizontal")
scale.pack()




root.mainloop()