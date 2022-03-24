from decimal import Decimal, getcontext

# incorrect


getcontext().prec = 100

t = 0
for i in range(2, 100):
	s = Decimal(i).sqrt()
	
	if s.as_integer_ratio()[1] != 1:
		for i in str(s)[2:]:
			t += int(i)
		print(t)

print(t)
