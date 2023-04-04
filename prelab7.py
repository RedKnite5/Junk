from sympy import *
#init_printing(use_unicode=True)



def B(n):
    return Rational(5, 2)/(pi*n)


var("n", positive=True, integer=True)
var("R1 R2 R3 w0 C w", positive=True)

var("Vs Vo")

values = [
    (R1, Rational(56)*100),
    (R2, Rational(56)*100),
    (R3, Rational(56)*100),
    (C,  Rational(10)**-7),
]


Vp = Vs * R3*C*w*I / (R3*C*w*I + 1)

Solved = solve((Vs-Vp)/R1 - (Vp-Vo)/R2, Vo)
H = Solved[0]/Vs

pprint(H)

#print(limit(H, w, oo))
#print(limit(H, w, 0))

pprint(abs(H))
mag = N(N(abs(H.subs(values))))
print("Mag:\n")
pprint(mag)

#phi = N(atan(im(H)/re(H))).subs(values)
print("Phi:\n")
#pprint(N(N(phi)))

print("\n"*3)
pprint(N(H.subs(values)))

print("\n")
pprint(log(H.subs(values)).as_real_imag()[1])


