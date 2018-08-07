import tkinter as tk
#   python stuff.py 

master = tk.Tk()

















b1 = tk.Button(master,text="b1")
b2 = tk.Button(master,text="b2")
b3 = tk.Button(master,text="b3")
b4 = tk.Button(master,text="b4")
b5 = tk.Button(master,text="b5")
b6 = tk.Button(master,text="b6")
b7 = tk.Button(master,text="b7")
b8 = tk.Button(master,text="b8")
b9 = tk.Button(master,text="b9")
b10 = tk.Button(master,text="b10")
b11 = tk.Button(master,text="b11")
b12 = tk.Button(master,text="b12")

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

b10.grid(row=3, column=0)
b11.grid(row=3, column=1)
b12.grid(row=3, column=2)


w=300
h=200

disp = tk.Canvas(master,width=w,height=h)

disp.grid(row=0, column=3, rowspan=4)

disp.create_rectangle(0,0,w,h,fill="black")

out = tk.Message(master,text="output",width=400)

out.grid(row=4, column=0, columnspan=4)


	
	

master.mainloop()