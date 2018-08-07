# euler4.py

def detect_palindrome(n):
	'''Return True if the string form of an object is a palindrome'''
	
	n = str(n)
	
	return(bool(n == "".join(reversed(n))))

def find_largest_palindrome():
	'''Return the largest palindrome number that is a multiple of two
	numbers that are digits digits long.'''
	
	l = []
	for i in range(999, 800, -1):
		for h in range(999, 800, -1):
			if detect_palindrome(i*h):
				l.append(i*h)
	return max(l)

