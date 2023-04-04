from sympy import *
init_printing(use_unicode=True)

var("t", real=True)
var("s")



Rs = Rational(270)
R1 = Rational(470)
R2 = Rational(100)
Rw = Rational(90)

V = Rational(5)

L = Rational(33, 1000)
C = Rational(1, 10**6)


expression = (Rational(9500, 93) + Rational(11, 620) * s) / (L * s*s + 190*s + 10**6)
pprint(expression)
out = inverse_laplace_transform(expression, s, t)
print(repr(out))
pprint(N(out).expand())



Il0 = V / (Rs + R1 + R2 + Rw)
Vc0 = Il0 * (Rw + R2)

Il0s = Il0 * L
s_coef = Il0s * 100 / L

print("here", s_coef * L)

a = (R2 + Rw) / L / 2

# Il0s * (s + a - a + Vc0 / Il0s)
const = Vc0 * 100 / L / s_coef - a
const = const * s_coef

print(float(const))

w = sqrt(Rational(10**6) / L - a*a)
print("w: ", float(w))
print("a: ", float(a))


c2 = const / w
print("s coef: ", float(s_coef))
print("constant coef: ", float(c2))

sin_coef = c2 / w
print(f"{float(sin_coef) = }")

print("mag: ", float((s_coef**2 + sin_coef**2)**.5))

#V_t = 6.597*10**-3 * exp(-2879*t)*sin(4692*t) + 1.146 * 10**-4 * exp(-2879*t)*cos(4692*t)

#plot(V_t, xlim=(0, 5*10**-3))

#print(V_t.subs(t, 0.000883346).evalf())
#print(V_t.subs(t, 0.00021378).evalf())



