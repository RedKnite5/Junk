#!/cygdrive/c/Users/RedKnite/AppData/Local/Programs/Python/Python38/python


# curses_learning.py
import curses
from curses import wrapper

class Snake(object):
	def __init__(self, len=1, pos=None):
		self.len = len
		if pos is None:
			self.pos = (40, 40)
		else:
			self.pos = pos
	
	def move(self, dir):
		pass
	



def main(stdscr):
	
	curses.curs_set(0)
	
	y, x = stdscr.getmaxyx()
	
	stdscr.addstr(y//2, x//2, "█", curses.A_BOLD)
	
	stdscr.refresh()
	
	
	while True:
		k = stdscr.getkey()
		
		pre_pos = stdscr.getyx()
		stdscr.move(0, 0)
		stdscr.clrtoeol()
		stdscr.move(*pre_pos)
		stdscr.addstr(0, 0, k)
		
		if k == "q":
			break
		
		if k in ("KEY_A2", "w"):
			stdscr.addstr(y//2-1, x//2, "█", curses.A_BOLD)
		
		stdscr.refresh()
	
	
	
	


curses.wrapper(main)









