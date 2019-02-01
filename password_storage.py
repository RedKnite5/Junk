# password_storage.py
import pickle
import random
import string

try:
	with open("password_vault.txt", "r") as file:
		table = pickle.load(file)
except FileNotFoundError:
	with open("password_vault.txt", "w+"):
		pass
	table = {}


def rand_str(
	length: int=4,
	charset: ty.Iterable="abcdefghijklmnopqrstuvwxyz") \
	-> str:
	'''Return a random string of length length from the character set
	charset.'''

	return "".join(
		charset[random.randint(
			0,
			len(charset) - 1)] for i in range(length))


def password_weak(password):
	if len(password) < 7:
		return True
	if not any(i in password for i in string.punctuation):
		return True
	if not any(i in password for i in string.ascii_uppercase):
		return True
	if not any(i in password for i in string.ascii_lowercase):
		return True
	if not any(i in password for i in string.digits):
		return True


def sign_up(name, password):
	if name in table:
		raise ValueError("Username already taken")
	elif password_weak(password):
		raise ValueError("Weak password")
	else:
		l = [rand_str(30, string.printable)]
		l.append(hash(l[0] + password))
		table{name} = tuple(l)
