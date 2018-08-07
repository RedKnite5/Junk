import mod,math,vol
# python stuff3.py



area = {}
a = True
while a:
	state = input("state: ")
	if state == "done":
		a = False
		break
	_range = input("range: ")
	range_ = _range.split("-")
	start = int(range_[0])
	end = int(range_[1])
	if state not in area:
		area[state] = []
	for j in range(start,end+1):
		z = "000"
		area[state].append(z[:-1*len(str(j))]+str(j))
print(area)
