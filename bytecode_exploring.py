import dis

with open("mem_fuckery.py", "r") as file:
	text = file.read()

code = compile(text, "mem_fuckery.py", "exec")

with open("bytecode.pyc", "w+") as file:
	dis.dis(code, file=file)

