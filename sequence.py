#  python sequence.py


class Sequence(object):
	def __init__(self, func, starting_vals):
		try:
			self.__values = list(starting_vals)
		except:
			self.__values = [starting_vals]
		self.func = func
		
	def next_item(self):
		self.__values.append(self.func(self.__values))
		return self.__values[-1]
	
	def __getitem__(self, key):
		last = key if isinstance(key, int) else key.stop
		
		while len(self.__values) < last:
			self.next_item()
		
		return tuple(self.__values[key])


def fib(seq):
	return seq[-1] + seq[-2]
	
s = Sequence(fib, (1, 1))
print(s[0:10])

