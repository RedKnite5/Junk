# ant.py

"""Langton's Ant"""

import curses
import time

from recordclass import recordclass

import numpy as np


class CursesScreen(object):
    def __enter__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)
        return self.stdscr

    def __exit__(self, exception_type, exception, trace):
        curses.echo()
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.endwin()

Point = recordclass("Point", ("x", "y"))

def modulo_class(modulo):
    class Tmp(int):
        def __new__(cls, *args, **kwargs):
            if super().__new__(cls, *args, **kwargs) >= modulo:
                return super().__new__(cls, *args, **kwargs) % modulo
            return super().__new__(cls, *args, **kwargs)

        def __add__(self, other):
            return self.__class__(super().__add__(other) % modulo)

        def __sub__(self, other):
            return self.__class__(super().__sub__(other) % modulo)

        def __mod__(self, other):
            return self.__class__(super().__mod__(other))

    Tmp.__name__ = f"ModuloClass_{modulo}"
    Tmp.__qualname__ = f"ModuloClass_{modulo}"
    return Tmp


Int4 = modulo_class(4)

class Map(object):
    def __init__(self, start=None):
        if start:
            self.state = start.state
            self.pos = start.pos
            self.orient = start.orient
        else:
            self.state = np.zeros((5, 5))
            self.pos = Point(self.state.shape[0] // 2, self.state.shape[1] // 2)
            self.orient = Int4(0)

    def move(self):
        if self.orient == 0:
            self.pos.y += 1
        elif self.orient == 1:
            self.pos.x += 1
        elif self.orient == 2:
            self.pos.y -= 1
        elif self.orient == 3:
            self.pos.x -= 1
        else:
            raise RuntimeError(f"self.orient must be 0, 1, 2, or 3. Not {self.orient}")
        if (
            self.state.shape[1] <= self.pos.x
            or self.pos.x < 0
            or self.state.shape[0] <= self.pos.y
            or self.pos.y < 0
        ):
            new_state = np.zeros((self.state.shape[0] * 2, self.state.shape[1] * 2))
            new_state[
                    new_state.shape[0] // 4:(new_state.shape[0] * 3) // 4,
                    new_state.shape[0] // 4:(new_state.shape[0] * 3) // 4
                    ] = self.state
            self.state = new_state
            self.pos.x += new_state.shape[1] // 4
            self.pos.y += new_state.shape[0] // 4

    def __iter__(self):
        return self

    def __next__(self):
        self.state[(self.pos.x, self.pos.y)] = int(not self.state[(self.pos.x, self.pos.y)])
        if self.state[(self.pos.x, self.pos.y)] == 1:
            self.orient += 1
            self.move()
        else:
            self.orient -= 1
            self.move()
        return self

    def __str__(self):
        return str(self.state)

    def display(self, steps=10):
        with CursesScreen() as stdscr:
            for step, screen in enumerate(self):
                if step == steps:
                    break
                stdscr.addstr(0, 0, "_" * (screen.state.shape[1] + 2))
                stdscr.addstr("\n")
                for col in screen.state:
                    stdscr.addstr("|")
                    for cell in col:
                        if cell:
                            stdscr.addstr("█")
                        else:
                            stdscr.addstr(" ")
                    stdscr.addstr("|\n")
                stdscr.addstr("‾" * (screen.state.shape[1] + 2))
                stdscr.addstr("\n")
                stdscr.refresh()
                time.sleep(.01)



if __name__ == "__main__":
    m = Map()
    m.display(1000)

