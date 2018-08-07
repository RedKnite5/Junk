import tkinter as tk
import colorsys
#   python stuff.py 

root = tk.Tk()

a = tk.Canvas(root,width=400,height=400)
a.pack()


load = tk.PhotoImage(file="timeline.ps")

a.create_image(200,200,image=load)

root.mainloop()