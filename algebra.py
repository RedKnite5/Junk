
from numbers import Real
from functools import reduce


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

    def __neg__(self):
        return Expression(op="*", left=-1, right=self)
    
    def __pos__(self):
        return self
    
    def __sub__(self, other):
        return self + (-other)
    
    def __rsub__(self, other):
        return Expression(op="+", left=other, right=-self)
    
    def __rmul__(self, other):
        return Expression(op="*", left=other, right=self)
    
    def __mul__(self, other):
        return Expression(op="*", left=self, right=other)
    
    def __truediv__(self, other):
        return self * (1/other)
    
    def __rtruediv__(self, other):
        return Expression(op="*", left=other, right=1/self)


class Expression(object):
    def __init__(self, op, left, right):
        # if op is a number then it it a value
        # if op is a symbol then it is a variable
        self.op = op
        

        if self.op == "+":
            self.args = []
            if getattr(left, "op", "") == "+":
                self.args.extend(left.args)
            else:
                self.args.append(left)
            if getattr(right, "op", "") == "+":
                self.args.extend(right.args)
            else:
                self.args.append(right)

            self.reduce_add()

        elif self.op == "*":
            self.args = []
            if getattr(left, "op", "") == "*":
                self.args.extend(left.args)
            else:
                self.args.append(left)
            if getattr(right, "op", "") == "*":
                self.args.extend(right.args)
            else:
                self.args.append(right)
            self.reduce_mul()
        elif isinstance(self.op, str):
            self.left = left
            self.right = right

    def __str__(self):
        if self.op == "+":
            return "+".join(map(str, self.args))
        elif self.op == "*":
            return "*".join(f"({x})" if getattr(x, "op", "") == "+" else str(x) for x in self.args)
        elif not isinstance(self.op, str):
            return str(self.op)
        
        return f"{self.left}{self.op}{self.right}"
    
    def __repr__(self):
        return f"Expression({self})"
    
    def __eq__(self, other):
        if self.op == other:
            return True
        elif type(self) != type(other):
            return False

        if self.op == other.op:
            if self.op in "+*":
                return self.args == other.args
            else:
                return self.left == other.left and self.right == other.right
        return False
    
    def Eval(self, **kwargs):
        if self.op == "+":
            return sum(evaluate(term, **kwargs) for term in self.args)
        elif self.op == "*":
            return reduce(lambda x, y: x * y, [evaluate(term, **kwargs) for term in self.args])
        else:
            raise ValueError("Unknown operator")
    
    def reduce_add(self):
        t = sum(x for x in self.args if isinstance(x, Real))
        self.args = [x for x in self.args if not isinstance(x, Real)]
        if t:
            self.args.append(t)
        
        print(f"Reducing {self}")

        key = {str(x): x for x in self.args}

        terms = {}
        # collect like terms
        for x in self.args:
            if getattr(x, "op", "") == "*":
                if isinstance(x.args[-1], Real):
                    print("x: ", x)
                    print("x/xargs", x / x.args[-1])
                    terms[str(x / x.args[-1])] = terms.get(str(x / x.args[-1]), 0) + x.args[-1]
                    print(f"{terms=}")
                    print("key:", str(x / x.args[-1]))
            else:
                terms[str(x)] = terms.get(str(x), 0) + 1
       
        new_args = []
        for term, coefficent in terms.items():
            if not coefficent:
                continue
            elif coefficent == 1:
                new_args.append(key[term])
            else:
                new_args.append(Expression(op="*", left=key[term], right=coefficent))

        self.args = new_args
        if not self.args:
            self.op = 0
        
        print("END")



    def reduce_mul(self):
        t = reduce(lambda a, b: a*b, (x for x in self.args if isinstance(x, Real)), 1)
        self.args = [x for x in self.args if not isinstance(x, Real)]
        
        if not t:
            self.op = 0
            return
        elif t != 1:
            self.args.append(t)
        
        # Distribute
        if len(self.args) == 2 and getattr(self.args[0], "op", "") == "+" and isinstance(self.args[1], Real):
            self.op = "+"
            self.args = [x * self.args[1] for x in self.args[0].args]
        
    
    def __neg__(self):
        return Expression(op="*", left=-1, right=self)
    
    def __pos__(self):
        return self
    
    def __add__(self, other):
        return Expression(op="+", left=self, right=other)
    
    def __radd__(self, other):
        return Expression(op="+", left=other, right=self)
    
    def __sub__(self, other):
        return self + (-other)
    
    def __rmul__(self, other):
        return Expression(op="*", left=other, right=self)
    
    def __mul__(self, other):
        return Expression(op="*", left=self, right=other)

    def __truediv__(self, other):
        return self * (1/other)
    
    def __rtruediv__(self, other):
        return Expression(op="*", left=other, right=1/self)



if __name__ == "__main__":

    x = Symbol("x")
    y = Symbol("y")

    #print(x-x)
    #a = x - y
    #print(a - a)

    print(-1*(x+y))

