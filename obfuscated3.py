#   obfuscated3.py

b=lambda r,b:\
(len(range(-r if\
r>0 else r,(-b,b)[b>0]))*(1\
if r+b>0 else -1)+((2*max(r,b) if r>0 else\
2*min(b,r)) if (b<0)!=(r<0) else 0))\
//(3 if 0 in (r,b) and (r<0 or b<0) else 1)

# b does integer addition
print(b(-5, 0))

'''
def this():
    from sys import _getframe as GF
    d = GF(1).f_locals
    L = 1
    while '.%d' % L in d:
        L += 1
    try:temp = d['.%d' % (L-1)].__next__()
    except:return 0
    print(L, temp)
    return temp
def a(c):return [this() if i>0 else 1 for i in range(10)]

thing = list(range(1, 7))
print(thing)
print(a(thing))
'''