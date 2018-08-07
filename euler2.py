# euler2.py

# sum the even fibonacci number less than 4 million

def third_fib():
	b , a = 1, 2
	
	while True:
		yield a
		for i in range(3):
			c = a + b
			b = a
			a = c

t = 0
for i in third_fib():
	if i < 4e6:
		t += i
	else:
		break
print(t)
