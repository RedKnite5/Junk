from PIL import ImageGrab
import tkinter as tk
#   python stuff.py
root = tk.Tk()

cv = tk.Canvas()
cv.pack()

cv.create_line(10,10,50,50)

cv.update()

def getter(widget):
    x=root.winfo_rootx()+widget.winfo_x()
    print(x)
    y=root.winfo_rooty()+widget.winfo_y()
    print(y)
    x1=x+widget.winfo_width()
    print(x1)
    y1=y+widget.winfo_height()
    print(y1)
    ImageGrab.grab().crop((x,y,x1,y1)).save("line.jpg")

getter(cv)
root.mainloop()