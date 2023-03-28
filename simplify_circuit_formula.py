from sympy import *
#init_printing(use_unicode=True)



var("n", positive=True, integer=True)
var("R1 R2 L1 L2 w0 C w", positive=True)
var("Vs")

num = Vs*L2*w*I

d1 = I*L2*w*(R2+L2*w*I)/(I*w*(L1+L2)+R2) + R1
d2 = L1*w*I + L2*w*I + R2

H = num / (d1 * d2 * Vs)

H_n = H.subs([(R1, 10), (R2, 10)]).subs(L2, L1).subs(L1, Rational(10)**-3).subs(w, n*pi)
H_1234 = [simplify(H_n.subs(n, i)) for i in range(1, 5)]

mags = [simplify(abs((h * 20_000/(pi*n)).subs(n, i+1))) for i, h in enumerate(H_1234)]
thetas = [simplify(atan(im(h) / re(h))+pi) for h in H_1234]


for i, m in enumerate(mags):
    print(f"Mag {i+1}: {N(m)}")

print("")
for i, t in enumerate(thetas):
    print(f"Theta {i+1}: {N(t)}")
