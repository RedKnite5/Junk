# scraping.py


from bs4 import BeautifulSoup
import requests
import re
import pickle
from urllib.parse import urljoin
from time import sleep


from graph import Graph

def convert_to_urls(links):
	return [i.get("href") for i in links]
		

def get_links(url):
	try:
		try:
			r = requests.get(url)
		except KeyboardInterrupt:
			exit()
		except:
			r = requests.get(url)
		
		soup = BeautifulSoup(r.text, features="lxml")
		
		urls = convert_to_urls(soup.find_all("a"))
		abs_urls = list(map(lambda a: urljoin(url, a), urls))

		return abs_urls
	
	except Exception as e:
		print("\nERROR: ", e)
		print(url, "\n")
		return []



if __name__ == "__main__":
	print("\n" * 5)

	with open("links.txt", "rb") as file:
		web, links = pickle.load(file)

	try:
		for i in range(2):
			print(len(links))
			collective_links = set()
			
			for link in links:
				if link in web.connections:
					continue
				
				print(link)	
				
				page_links = set(get_links(link))
				
				collective_links = collective_links.union(page_links)
				for j in page_links:
					web.add_connection(link, j)
				
			links = collective_links
	except:
		print("Uncaught exception!\n")
	else:
		print("Success!")
	finally:
		with open("links.txt", "wb") as file:
			pickle.dump((web, collective_links), file)


	print("done")





