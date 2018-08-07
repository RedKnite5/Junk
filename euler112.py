# euler112.py

def bouncy(n):
	'''Detect if n is 'bouncy'.'''

	s = str(n)
	inc = dec = True

	last = int(s[0])
	for i in s:
		i = int(i)
		if i > last:
			dec = False
		elif i < last:
			inc = False
		if not (dec or inc):
			return True
		last = i
	return False


def find_bouncy_prop(n):
	
	i = 1
	c = 0
	p = 0
	while p != n:
		if bouncy(i):
			c += 1
		p = c / i
		i += 1
	return i - 1

x = find_bouncy_prop(.99)
print(x)


