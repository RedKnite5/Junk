import mod,sys
# python words_to_num.py

number = "twelve billion seven hundred and five million two hundred and sixty three thousand five hundred and nineteen"
number = mod.lower_input("words")
words = number.split()

digits = {
"one":"1",
"two":"2",
"three":"3",
"four":"4",
"five":"5",
"six":"6",
"seven":"7",
"eight":"8",
"nine":"9"}

teens = {
"ten":"10",
"eleven":"11",
"twelve":"12",
"thirteen":"13",
"fourteen":"14",
"fifteen":"15",
"sixteen":"16",
"seventeen":"17",
"eighteen":"18",
"nineteen":"19"}

tens = {
"twenty":"20",
"thirty":"30",
"fourty":"40",
"fifty":"50",
"sixty":"60",
"seventy":"70",
"eighty":"80",
"ninety":"90"}

higher = ["thousand","million","billion","trillion"]

def repl_list(dict):
	for key,num in dict.items():
		for i in range(len(words)):
			if words[i] == key:
				words[i] = num
				
				
def commas(input):
	init_len = len(input)
	for l in range(init_len):
		i = init_len-l
		if l%3 == 0 and i != 0:
			input = input[:i] + "," + input[i:]
	if input[0] == ",":
		input = input[1:]
	if input[len(input)-1] == ",":
		input = input[:len(input)-1]
	return(input)
	
def final(end):	
	val = commas(end)		
	print(val)
	print(float(end))
	sys.exit()
	


if number == "zero":
	final("0")
			
repl_list(digits) #convert digits
repl_list(tens) #convert the tens
	
for i in range(len(words)):  #add ones and tens
	try:
		if len(words[i]) == 2:
			words[i] = int(words[i])+int(words[i+1])
			words.pop(i+1)
	except:
		pass

		
		
repl_list(teens)


print("words list",words)
for i in range(len(words)):  #convert and add hundreds
	try:
		if words[i] == "hundred":
			words[i-1] = 100*int(words[i-1])
			words.pop(i)
	except:
		pass
		
		
for i in range(len(words)):  #deal with "and"
	try:
		if words[i] == "and":
			if words[i-1] in higher:
				words.pop(i)
				print("words",words)
			else:
				print("else",words)
				words[i-1] = int(words[i-1])+int(words[i+1])
				words.pop(i)
				words.pop(i)
	except:
		pass
		
print("after and",words)
		
for i in range(len(words)): #thousands, millions, etc.
	try:
		for d in range(len(higher)):
			if words[i] == higher[d]:
				words[i-1] = int(words[i-1])*10**(3*(d+1))
				words.pop(i)
	except:
		pass
		
for i in range(len(words)): #convert to integers
	words[i] = int(words[i])
	

end = 0
for i in words:
	end = end + i
print("end",end)

end = str(end)



final(end)






