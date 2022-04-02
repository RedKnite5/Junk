


def evaluate(expression, **kwargs):
    try:
        return expression.Eval(**kwargs)
    except AttributeError:
        return expression

class Symbol(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __hash__(self):
        return hash(self.name)
    
    def Eval(self, **kwargs):
        return kwargs.get(self.name, self)

    def __add__(self, other):
        return Expression(op="+", left=self, right=other)

    def __radd__(self, other):
        return Expression(op="+", left=other, right=self)


class Expression(object):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left}{self.op}{self.right}"
    
    def Eval(self, **kwargs):
        if self.op == "+":
            return evaluate(self.left, **kwargs) + evaluate(self.right, **kwargs)
        else:
            raise ValueError("Unknown operator")
    
    def __add__(self, other):
        return Expression(op="+", left=self, right=other)





x = Symbol("x")
y = Symbol("y")

xy = x + y + 1

print(xy)
print(xy.Eval(x=1))
