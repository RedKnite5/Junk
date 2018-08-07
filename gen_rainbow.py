import itertools, hashlib,mod

def iter_all_strings(*arg):
	if len(arg) > 0:
		charset=arg[0]
		
	else:
		charset = [chr(i) for i in range(32,127)]
	size = 1
	while True:
		for s in itertools.product(charset, repeat=size):
			yield "".join(s)
		size +=1

def rainbow_table(file_name,*arg):
	if len(arg) > 1:
		set = arg[1]
	else:
		set = [chr(i) for i in range(32,127)]
	if len(arg) > 0:
		end_point = arg[0]
	else:
		end_point = set[len(set)-1]
		
	
	open(file_name,"w+").close()
	data = open(file_name,"a")

	for s in iter_all_strings(set):
		string = ""
		hash = hashlib.sha512()
		hash.update(s.encode("utf-8"))
		string += s
		string += " = "
		string += str(hash.hexdigest())
		string += "\n"
		data.write(string)
		if s == end_point:
			data.close()
			break

			
file = open("rainbow.txt","w+")
file.truncate()
file.close
rainbow_table("rainbow.txt","a",mod.ascii_charset)