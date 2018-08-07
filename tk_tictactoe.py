import tkinter as tk
#   python stuff.py

root = tk.Tk()


spaces = [tk.Canvas(root,width=50,height=50) for i in range(9)]

spaces[0].grid(row=0, column=0)
spaces[1].grid(row=0, column=1)
spaces[2].grid(row=0, column=2)

spaces[3].grid(row=1, column=0)
spaces[4].grid(row=1, column=1)
spaces[5].grid(row=1, column=2)

spaces[6].grid(row=2, column=0)
spaces[7].grid(row=2, column=1)
spaces[8].grid(row=2, column=2)



root.mainloop()

