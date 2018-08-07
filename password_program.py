import mymod, hashlib, pickle, sys

def start():
	passwords = pickle.load(open("passwords.txt","rb"))
	print("What do you want to do?")
	act = mymod.lower_input()
	if act == "sign in":
		sign_in()
	elif act == "login":
		login()
	elif act == "clear":
		passwords.clear()
		pickle.dump(passwords, open("passwords.txt","wb"))
	else:
		print("ERROR")
		sys.exit()

def sign_in():
	passwords = pickle.load(open("passwords.txt","rb"))
	info = []
	print("Username: ")
	user = input()
	if user == "exit":
		sys.exit()
	if user in passwords:
		print("User already exists.")
		store_passwords()
	print("Password: ")
	password = input()
	salt = mymod.rand_str(20,mymod.ascii_charset)
	password += salt
	info.append(salt)
	info.append(hashlib.sha512(password).hexdigest())
	passwords[user] = [info[0],info[1]]
	pickle.dump(passwords, open("passwords.txt","wb"))
	
	del info[:]
	del user
	del password
	del salt

def login():
	passwords = pickle.load(open("passwords.txt","rb"))
	print("Username: ")
	user = input()
	if user == "exit":
		sys.exit()
	if user not in passwords:
		print("No such user.")
		start()
	print("Password: ")
	password = input()
	hash_in = password + passwords[user][0]
	hash = hashlib.sha512(hash_in)
	if hash.hexdigest() == passwords[user][1]:
		print("Correct!")
	else:
		print("Incorrect")
		login()
	
	
start()