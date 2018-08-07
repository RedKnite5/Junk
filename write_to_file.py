# write_to_file.py

def write_to_file(text_in, filename, cutoff = 72):
	text = text_in
	print(text)
	end = 0

	
	with open(filename, "w") as file:
		while text:
			text = text[end:]
			part = text[:cutoff]

			if len(text) < cutoff:
				file.write(text)
				end = len(text)
				
			elif " " not in part or text[cutoff] == " ":
				file.write(part + "\n")
				if text[cutoff] == " ":
					end = cutoff + 1
				else:
					end = cutoff
			else:
				space = part.rfind(" ")
				file.write(part[:space] + "\n")
				end = space + 1
