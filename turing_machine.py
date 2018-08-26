#   stuff.py
# cd C:\Users\Max\Documents\Python\ReCalc
# cd C:\Users\Max\Documents\Python\Junk


class Tape(object):
	__slots__ = ["symbols"]
	def __init__(self, symbols={}):
		self.symbols = symbols

	def read(self, address: int) -> int:
		return self.symbols.get(address, 0)

	def write(self, address: int, value: int) -> None:
		if not value:
			if address in self.symbols:
				del self.symbols[address]
		else:
			self.symbols[address] = value

class Machine(object):
	'''A turing machine class.'''

	def __init__(self, states, tape):
		self.states = states
		self.states[-1] = self.halt
		self.state = self.states[0]
		self.tape = tape
		self.address = 0
		self.halted = False

	def switch(self, state):
		self.state = self.states[state]

	def move(self, direction):
		assert direction in (-1, 0, 1)
		self.address += direction

	def write(self, value):
		self.tape.write(self.address, value)

	def do(self):
		if not self.halted:
			self.state(self, self.tape.read(self.address))
			return
		print("halted")	

	def halt(self, *args):
		self.halted = True
		return self.tape

def make_state(dictionary):
	'''Make a state function for a turing machine.'''

	def state(machine, data):
		inst = dictionary[data]
		machine.write(inst["write"])
		machine.move(inst["move"])
		machine.switch(inst["switch"])

	return state




state_info = {0 : {"write": 1, "move": 1, "switch": 0}, 1: {"write": 1, "move": 1, "switch": -1}}
states = {0: make_state(state_info)}
m = Machine(states, Tape())
while not m.halted:
	m.do()
	print(m.tape.symbols)
