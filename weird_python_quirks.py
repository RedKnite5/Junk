#   weird_python_quirks.py

condition = False
print(("what", "the")[condition])

a = bool("s")
b = bool(2)
print(a+b)

g = 5,
print(g)

def counter():
	if hasattr(counter, "count"):
		counter.count += 1
	else:
		counter.count = 1
	print(counter.count)

for i in range(5):
	counter()

print("5" + "5",)
print(f"g: {g!r}")
