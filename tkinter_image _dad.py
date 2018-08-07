import tkinter as tk
import PIL
from PIL import Image
from PIL import ImageTk
#   python tkinter_image_dad.py



root = tk.Tk()


can = tk.Canvas(root,width=800,height=800)
can.pack()

#pic = Image.open("worm_characters_symbols.png")
#logs = ImageTk.PhotoImage(image=pic)

#can.create_image(200,200,image=logs)


root.mainloop()