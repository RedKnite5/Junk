import pickle
#  python test.py

file = open("popular_words100.txt")
words = []
for i in file:
	print(i)
	words.append(i[:-1])
print(words)

pickle.dump(words,open("pickled_pop_words.txt","wb"))