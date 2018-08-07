
#   python stuff.py

tree = {}

def col(a):
	steps = 0
	while a != 1:
		print(a)
		if a%2 == 0:
			steps += 1
			tree[a] = a/2
			a = a/2
		else:
			steps += 2
			tree[a] = 3*a+1
			print(3*a+1)
			a = (3*a+1)/2
			tree[2*a] = a
	print(1)
	print("steps: ",steps)

i = 1
while i < 100:
	col(i)
	i+=1
print(tree)