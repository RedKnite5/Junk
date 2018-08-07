import tkinter as tk
import PIL
#from PIL import Image
#from PIL import ImageTk
#   python tkinter_image.py



root = tk.Tk()


can = tk.Canvas(root,width=800,height=800)
can.pack()

pic = PIL.Image.open("worm_characters_symbols.png")
tkpic = PIL.ImageTk.PhotoImage(pic)

can.create_image(400,400,image=tkpic)


root.mainloop()