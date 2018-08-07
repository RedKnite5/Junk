import sys, math, random, itertools, hashlib, pickle
#import timeit, enchant, urllib2, nltk, Tkinter, _thread
#from tkinter import *
#from bs4 import BeautifulSoup

"""
cd documents
cd python

"""

#words = pickle.load(open("list_of_Eng_words.txt","rb"))
ascii_charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers_set = "0123456789"
symbols_set = "`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? " 
pi = 3.1415926535897
tau = 6.2831853071796
e = 2.71828182846
phi = 1.61803398875



def instructions():
	inst = open("mod_instructions.txt","r")
	print(inst.read())
	inst.close()
	return

def lower_input(*arg):
	if len(arg) == 1:
		print(arg[0])
	y = input()
	x = y.strip()
	return x.lower()
	
def devar(x):
	return x
	
def parse(text_0, *arg):
	if len(arg) == 1:
		sep = arg[0]
	else:
		sep = " "
	text = text_0.strip()
	text_1 = text + sep
	word = sep + text_1
	li = []
	s = 0
	i = 0
	while i < len(word):
		if word[i] == sep:
			new = ""
			for h in range(s+1, i):
				new += word[h]
			li.append(new)
			s = i
		i += 1
	li.pop(0)
	return li
	
def factor(number):
	potential_factors = []
	factors = []
	num_sqrt = int(math.ceil(number**.5))+1
	for x in range(1,num_sqrt):
		potential_factors.append(x)
	for x in potential_factors:
		divisable =  number % potential_factors[x-1] == 0
		if divisable:
			factors.append(x)
			factors.append(number/x)
	if factors[len(factors)-1] == factors[len(factors)-2]:
		factors.pop()
	answer=[]
	for x in range(len(factors)):
		answer.append(factors[x])
	del factors[:]
	del potential_factors[:]
	del num_sqrt
	return answer
	
def quad_form(quad_a, quad_b, quad_c):
	quad_form_ans = []
	rand = ((quad_b**2) - 4*quad_a*quad_c)**.5
	quad_form_ans.append(((-1*quad_b)+rand)/(2*quad_a))
	quad_form_ans.append(((-1*quad_b)-rand)/(2*quad_a))
	return quad_form_ans

def pyth(a,b):
	c_sqrd = (a**2)+(b**2)
	c = c_sqrd**.5
	return c
	
def un_pyth(a,c):
	b_sqrd = (c**2)-(a**2)
	b = b_sqrd**.5
	return b

def insert_string(main_str,insert,place):
	result = ""		
	if place>0:
		for i in itertools.islice(main_str,0,place):
			result += i
	result+=insert
	for i in itertools.islice(main_str,place,len(main_str)):
		result += i
	print(result)

def factorial(n):
	ans = 1
	for i in range(1,n+1):
		ans = ans * i
	return ans
	
def permute(n,r):
	if r > n:
		raise ValueError("second argument: %d is greater than first argument: %d"%(r,n))
	else:
		ans = factorial(n)/factorial(n-r)
		return ans
		
def choose(n,r):
	if r > n:
		raise ValueError("second argument: %d is greater than first argument: %d"%(r,n))
	else:
		ans = permute(n,r)/factorial(r)
		return ans
	
def rand_str(*arg):
	if len(arg) > 0:
		length = arg[0]
	else:
		length = 4
	if len(arg) > 1:
		charset = arg[1]
	else:
		charset = lowercase
		
	set_size = len(charset)
	string = ""
	for i in range(length):
		string += charset[random.randint(0,set_size-1)]
	return string
	
def start_substr(substr,string):
	if substr not in string:
		raise ValueError("Substring not in string.")
	for i in range(len(string)):
		if substr[0] == string[i]:
			start = True
			for j in range(len(substr)):
				if substr[j] != string[i+j]:
					start = False
			if start == True:
				return i

def str_start(begin,string,*args):
	if len(args) > 0:
		place = args[0]
	bool = True
	for num,letter in enumerate(begin,place):
		try:
			if letter != string[num]:
				bool = False
		except:
			bool = False
			break
	return bool
			


