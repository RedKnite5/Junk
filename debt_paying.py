# debt_paying.py

import tkinter as tk

root = tk.Tk()


debt_words = tk.Label(root, text="Starting Debt: ")
debt_words.grid(row=0, column=0)

debt_box = tk.Entry(root)
debt_box.grid(row=0, column=1)

intrest_words = tk.Label(root, text="Annual Intrest Rate: ")
intrest_words.grid(row=1, column=0)

intrest_box = tk.Entry(root)
intrest_box.grid(row=1, column=1)

time_words = tk.Label(root, text="Number of Months: ")
time_words.grid(row=2, column=0)

time_box = tk.Entry(root)
time_box.grid(row=2, column=1)

payment_words = tk.Label(root, text="Payment Amount: ")
payment_words.grid(row=3, column=0)

payment_box = tk.Entry(root)
payment_box.grid(row=3, column=1)


def calculate():
	debt = debt_box.get()
	rate = intrest_box.get()
	duration = time_box.get()
	amount = payment_box.get()
	
	calculating = "time" if duration == "" else "amount"
	
	print(calculating)



calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.grid(row=4, column=0, columnspan=2)


root.mainloop()
