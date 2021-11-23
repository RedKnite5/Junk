# replace_class.py

class A(object):
    def __init__(self):
        self.x = 5

class B(object):
    pass

b = B()
a = A()

print(type(a.__weakref__))
print(hasattr(a, "__weakref__"))
'''
for attr in dir(a):
    
    setattr(a, attr, getattr(b, attr))
    print(f"{attr}: {getattr(a, attr)}")

print(type(a))
'''