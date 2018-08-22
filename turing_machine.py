#   stuff.py
# cd C:\Users\Max\Documents\Python\ReCalc
# cd C:\Users\Max\Documents\Python\Junk


class Tape(object):
	def __init__(self, ones=[]):
		self.ones = list(ones)

	def read(self, address: int) -> int:
		if address in self.ones:
			return 1
		else:
			return 0

	def write(self, address: int, value: int) -> None:
		if not value:
			if address in self.ones:
				del self.ones[address]
		else:
			self.ones.append(address)

class Machine(object):
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
			
	
	def halt(self, data, other):
		#print(self, self2, data)
		self.halted = True
		return self.tape

def make_state(
	write_if_zero,
	move_if_zero,
	change_state_if_zero,
	write_if_one,
	move_if_one,
	change_state_if_one):
	
		def state(machine, data):
			if data:
				machine.write(write_if_one)
				machine.move(move_if_one)
				machine.switch(change_state_if_one)
				return
			machine.write(write_if_zero)
			machine.move(move_if_zero)
			machine.switch(change_state_if_zero)
		
		return state




state_info = (1, 1, 0, 1, 1, -1)
states = {0: make_state(*state_info)}
m = Machine(states, Tape())
while not m.halted:
	m.do()

print(m.tape.ones)
