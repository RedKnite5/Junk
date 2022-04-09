


# take the derivative of a polynomial
def derivative(poly):
    return Polynomial([a*i for i, a in enumerate(poly.coefficients[1:])])

#create a polynomial class
class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
        self.degree = len(coefficients) - 1
    def __call__(self, x):
        return sum(a*x**i for i, a in enumerate(self.coefficients))
    def __add__(self, other):
        return Polynomial([a+b for a, b in zip(self.coefficients, other.coefficients)])
    def __mul__(self, other):
        return Polynomial([a*b for a, b in zip(self.coefficients, other.coefficients)])
    def __str__(self):
        return ' + '.join(['{}x^{}'.format(a, i) for i, a in enumerate(self.coefficients)])
    def __repr__(self):
        return 'Polynomial({})'.format(self.coefficients)
    def __eq__(self, other):
        return self.coefficients == other.coefficients
    def __ne__(self, other):
        return self.coefficients != other.coefficients

# test the polynomial class
def test_polynomial():
    p = Polynomial([1, 2, 3])
    assert p(0) == 1
    assert p(1) == 2
    assert p(2) == 3
    assert p(3) == 6
    assert p(4) == 10

    q = Polynomial([-1, 0, 1])

    assert p + q == Polynomial([0, 2, 4])

if __name__ == '__main__':
    test_polynomial()
    print('All tests passed')

