


s = "hello"

f = lambda s: sum((ord(l) for l in s))
print(f(s))