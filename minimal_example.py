


def remember(self, string):
    print(string)
    type(self).called += 1
    self.inst_called += 1


def init(self):
    self.inst_called = 0

#List = type("List", (object,), {"called": 0, "__init__": init, "remember": remember})


def find():
    return type("List", (object,), {"called": 0, "__init__": init, "remember": remember})()

def call_both(f):
    l = f()
    l.remember("foo")


call_both(find)

print("called: ", find().called)
print("inst_called: ", find().inst_called)
