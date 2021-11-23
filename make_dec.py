# make_dec.py

funcs = {
"add": "+", "sub": "-", "mul": "*", "div": "/", "floordiv": "//", "truediv": "/",
"mod": "%", "pow": "**", "lshift": "<<", "rshift": ">>", "and": "&", "or": "|",
"xor": "^",
}

s = "{"
s2 = ""
for i in funcs:
	s += "{f}: \"__{f}__\", ".format(f=i)
	
	s2 += '''
		def {f}(self, other):
			return func(self.__dict__[arg]) {o} other
		def r{f}(self, other):
			return other {o} func(self.__dict__[arg])
		def i{f}(self, other):
			return func(self.__dict__[arg]) {o} other'''.format(f=i, o=funcs[i])

print(s2)
print(s + "}")