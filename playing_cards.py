#   playing_cards.py
import random

suits = ("spades", "clubs", "hearts", "diamonds")
kinds = ("ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king")

deck = []
for i in suits:
	for k in kinds:
		deck.append(k + " of " + i)


def draw(number):
	cards = []
	this_deck = []
	this_deck[:] = deck[:]
	for i in range(number):
		r = random.randint(0,len(this_deck) - 1)
		cards.append(this_deck[r])
		del this_deck[r]
		if not this_deck:
			this_deck[:] = deck[:]
	return(cards)


print(draw(2))


