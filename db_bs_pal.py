#  db_bs_pal.py



def check_num(n):
	return str(n) == str(n)[::-1] and bin(n)[2:] == bin(n)[:1:-1]
	
def make_palis(n):
	palis = []
	for i in range(10):
		palis.append(int(f"{n}{i}{str(n)[::-1]}"))
	return palis


palis = set()
for i in range(1, 1000):
	if len(str(i)) <= 2:
		if check_num(i):
			palis.add(i)
	for j in make_palis(i):
		if check_num(j):
			palis.add(j)

print(sum(palis))
#print(bin(585)[2:], bin(585)[:1:-1])