#!C:\Users\RedKnite\AppData\Local\Programs\Python\Python38\python

# stuff.py



import cProfile



from bs4 import BeautifulSoup
import requests
import re
import pickle
from urllib.parse import urljoin
from multiprocessing import Pool, freeze_support
from timeit import timeit


from graph import Graph

web = Graph()

def convert_to_urls(links):
	return [i.get("href") for i in links]
		

def get_links(url):
	global web
	
	print(url)
	
	try:
		r = requests.get(url)
		#except KeyboardInterrupt:
		#	exit()
		#except:
		#	r = requests.get(url)
		
		soup = BeautifulSoup(r.text, features="lxml")
		
		urls = convert_to_urls(soup.find_all("a"))
		#abs_urls = map(lambda a: urljoin(url, a), urls)
		
		#for j in abs_urls:
		#	web.add_connection(url, j)

		#return abs_urls
	
	#except KeyboardInterrupt:
	#	exit()
	except Exception as e:
		print("\nERROR: ", e)
		print(url, "\n")
		return



def func(pools):
	global web
	print("\n" * 5)

	with open("links.txt", "rb") as file:
		web, links = pickle.load(file)
	links = tuple(links)[:300]

	#try:
	for i in range(1):
		print(len(links))
		collective_links = set()
		
		#for link in links:
		#	if link in web.connections:
		#		continue
			
		with Pool(pools) as p:
				#pass
			collective_links = tuple(set(p.map(get_links, links)))
			
		links = collective_links
	'''
	except Exception as e:
		print("Uncaught exception!\n")
		raise e
	else:
		print("Success!")
	finally:
		pass

	'''
	print("done")
	


if __name__ == "__main__":
	t1 = timeit("func(8)", number = 2, globals = {"func": func})
	t2 = timeit("func(1)", number = 2, globals = {"func": func})
	print("t1: ", t1)
	print("t2: ", t2)
	

	
	


'''
from graph import Graph

import pickle
from pprint import pprint


with open("links.txt", "rb") as file:
	web = pickle.load(file)

pprint(web.connections)
'''

