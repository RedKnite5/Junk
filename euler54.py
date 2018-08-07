# euler54.py

filename = "C:\\Users\\Max\\Dropbox\\Python\\poker.txt"

def check_equal(iterator):
	'''Check if all elements of a list are equal.'''
	
	return(len(set(iterator)) <= 1) # content must be hashable

def check_straight(values):
	'''Check'''
	
	if set(values) == set(range(min(values), min(values) + 5)):
		return(max(values))
	elif set(values) == set((14, 2, 3, 4, 5)):
		return(5)
	return(False)

def convert_to_dict(lst):
	'''Convert to dictonary with elemnts as keys and count as value.'''
	
	d = {}
	for i in lst:
		if i in d:
			d[i] = d[i] + 1
		else:
			d[i] = 1
	return(d)


class Hand(object):
	card_values = {
		"2": 2, "3": 3, "4": 4, "5": 5, "6":6, "7": 7, "8": 8,
		"9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14,
	}

	def __init__(self, h):
		self.cards = h.split()
		
		self.values = tuple(map(lambda a: Hand.card_values[a[0]], self.cards))
		self.suits = tuple(map(lambda a: a[-1], self.cards))
		
		self.counted_cards = convert_to_dict(self.values)
		
		self.flush = check_equal(self.suits)
		
		self.straight = check_straight(self.values)
		
		self.straight_flush = self.flush and self.straight
		
		self.four = [k for k, v in self.counted_cards.items() if v == 4]
		
		self.three = [k for k, v in self.counted_cards.items() if v == 3]
		
		self.pairs = [k for k, v in self.counted_cards.items() if v == 2]
		
		self.fullhouse = (self.three[0], self.pairs[0]) if self.three and self.pairs else False
		
		if self.straight_flush:
			self.highest = 8
			#print("straight flush")
		elif self.four:
			self.highest = 7
			#print("four of a kind")
		elif self.fullhouse:
			self.highest = 6
			#print("fullhouse")
		elif self.flush:
			self.highest = 5
			#print("flush")
		elif self.straight:
			self.highest = 4
			#print("straight")
		elif self.three:
			self.highest = 3
			#print("three of a kind")
		elif len(self.pairs) == 2:
			self.highest = 2
			#print("two pairs")
		elif self.pairs:
			self.highest = 1
			#print("one pair")
		else:
			self.highest = 0
			#print("high card")
		
		
	def __gt__(self, other):
		if self.highest > other.highest:
			return(True)
		elif self.highest < other.highest:
			return(False)
		else:
			if self.highest == 8:
				return(self.straight_flush > other.straight_flush)
			elif self.highest == 7:
				if self.four != other.four:
					return(self.four > other.four)
				return(min(self.values, key=self.values.count) > min(other.values, key=other.values.count))
			elif self.highest == 6:
				if self.fullhouse[0] != other.fullhouse[0]:
					return(self.fullhouse[0] > other.fullhouse[0])
				return(self.fullhouse[1] > other.fullhouse[1])
			elif self.highest == 5:
				return(sorted(self.flush, reverse=True) == sorted((sorted(self.flush, reverse=True), sorted(other.flush, reverse=True)))[1])
			elif self.highest == 4:
				return(self.straight > other.straight)
			elif self.highest == 3:
				return(self.three > other.three)
			elif self.highest == 2:
				if max(self.pairs) != max(other.pairs):
					return(max(self.pairs) > max(other.pairs))
				if min(self.pairs) != min(other.pairs):
					return(min(self.pairs) > min(other.pairs))
				return(min(self.values, self.values.count) > min(other.values, other.values.count))
			elif self.highest == 1:
				if self.pairs != other.pairs:
					return(self.pairs[0] > other.pairs[0])
				return(sorted(self.values, reverse=True) == sorted((sorted(self.values, reverse=True), sorted(other.values, reverse=True)))[1])
			else:
				#print(sorted((sorted(self.values, reverse=True), sorted(other.values, reverse=True))), self.values)
				return(sorted(self.values, reverse=True) == sorted((sorted(self.values, reverse=True), sorted(other.values, reverse=True)))[1])

#x = Hand("3H 7H 6S KC JS") > Hand("QH TD JC 2D 8S")
#print(x)


with open(filename, "r") as file:
	wins = 0
	for count, line in enumerate(file.readlines()):
		#print("{count} Hand 1: {0} > Hand 2: {1} {2}".format(line[:15], line[15:], Hand(line[:15]) > Hand(line[15:-1]), count=count+1))
		wins += Hand(line[:15]) > Hand(line[15:])
		#input()
	print(wins)
