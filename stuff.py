#   stuff.py

b=lambda r,b:\
len(range(-r if\
r>0 else r,(-b,b)[b>0]))*(1\
if r+b>0 else -1)

print(b(1,-2))