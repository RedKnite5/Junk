# exec_dict.py


m = {"__builtins__": {"three": 3, "four": 4, "print": print}}
m["__builtins__"]["m"] = m

s = """
print(three)
m["__builtins__"] = {"print": print, "three": 4}
print(three)
"""

exec(s, m["__builtins__"])