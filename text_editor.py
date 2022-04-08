
import time
import tkinter as tk
import tkinter.font as tkFont
from functools import partial
from typing import Text
from collections import deque


class Coordinate:
    def __init__(self, index):
        self.index = index

    def __get__(self, instance, owner):
        return instance.cursor[self.index]
    
    def __set__(self, instance, value):
        instance.cursor[self.index] = value

class CurrentLine:
    def __get__(self, instance, owner):
        return instance.lines[instance.y]
    
    def __set__(self, instance, value):
        self.lines[instance.y] = value

class TextArray:
    x = Coordinate(0)
    y = Coordinate(1)
    current_line = CurrentLine()


    def __init__(self):
        self.lines = deque([deque()])
        self.cursor = [0, 0]  # x, y

    def insert(self, char):
        self.current_line.insert(self.x, char)
        self.x += 1
    

    


class TextEditor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text Editor")
        self.root.geometry("400x400")

        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.text = TextArray()
        self.font_size = 12

        self.canvas.create_line(
            self.text.x + self.font_size,      # x1
            self.text.y + self.font_size,      # y1
            self.text.x + self.font_size,      # x2
            self.text.y + 2 * self.font_size,   # y2
            tag="cursor"
        )
        self.canvas.focus_set()

        self.bindings()
    
    def bindings(self):
        self.canvas.bind("<Key>", self.key_press)
        self.canvas.bind("<Button-1>", self.mouse_press)

    def update_cursor(self):
        self.canvas.moveto(
            "cursor",
            (self.text.x + 1) * self.font_size,
            (self.text.y + 1) * self.font_size
        )

    def key_press(self, event):
        self.text.insert(event.char)
        print(f"writing {event.char}")

        self.canvas.delete(f"line_{self.text.y}")
        self.canvas.create_text(
            self.font_size,                        # x
            self.font_size * (self.text.y + 1),    # y
            text="".join(self.text.current_line),
            anchor='nw',
            font=('TkMenuFont', self.font_size),
            fill='black',
            tag=f"line_{self.text.y}"
        )
        self.update_cursor()



    def mouse_press(self, event):
        print("click")


    def mainloop(self):
        self.root.mainloop()



def main():
    t = TextEditor()

    t.mainloop()

if __name__ == "__main__":
    main()


