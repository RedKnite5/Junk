# obscured.py

def p(item, l=[]):
    l.append(item)
    if len(l) == 5:
        print("".join(l))

# 4 1 8 8 11
print(tuple(map(lambda a: chr(int(a) + 100), ('1' * (1<<(i-1)//2) if not i & 1 else 1 << i for i in range(1, 6)))))

class O(int):
    i = None
    def __new__(*a):
        if not isinstance(O.i, O):
            O.i = int.__new__(O, 1)
        return O.i
    def __radd__(*a):
        return O() if not a[1] else a[1] + 1
    def __sub__(*a):
        return a[1]


def f(i):
    global prev
    pr = prev
    
    n = globals().update(
        prev=(
            pr
             + (((1<<(i-prev))) == (1<<3)) if pr else (0 if pr == O() else O())
        )
    )
    return True if n else False


prev = 0
#n = map(lambda a: chr(int(a) + 100), ('1' * (1<<(i-1)//2) if not (i-prev) & 1 else 1 << i-prev + (lambda pr=prev:True if globals().update(prev=(pr+(((1<<(i-prev))) == (1<<3)) if pr else (0 if pr == O() else O()))) else False)() for i in range(1, 6)))

# new
n = map(lambda a: chr(int(a) + 100), ('1' * (1<<(i-1)//2) if not (i-prev) & 1 else 1 << i-prev + f(i) for i in range(1, 6)))
for i in n:
    p(i)