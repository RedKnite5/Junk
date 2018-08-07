# -*- coding: utf-8 -*-
import urllib.request, urllib.error, urllib.parse, sys, re
from bs4 import BeautifulSoup as BSoup
# python scraping_junk.py


#reload(sys)  
#sys.setdefaultencoding('utf8')

count = 0
start_url = "https://parahumans.wordpress.com/2011/06/14/gestation-1-2/"


def worm(url):
	global count
	if count > 3:
		exit()
	count += 1
	
	page = urllib.request.urlopen(url)
	soup = BSoup(page, "html.parser")
	soup.prettify().encode("utf-8")

	title = str(soup.title.get_text())
	title_ = title[:-6]
	title = title_ + ".txt"

	worm = open(title,"w+")
	worm.write(str(soup.encode("utf-8")))
	worm.close()

	aline = 0
	worm = open(title,"r+")
	d = worm.readlines()
	worm.seek(0)
	for i in d:
		print(len(d))
		if "\"Last Chapter\"" in i:
			aline += 1
		if aline == 2 or str(soup.title) in i:
			worm.write(i)
	worm.truncate()
	worm.close()

	tagged = "file:///C:/Users/Max/Dropbox/Python/Worm/"
	tagged += title
	tagged_worm = urllib.request.urlopen(tagged)
	worm_soup = BSoup(tagged_worm, "html.parser")
	worm_soup.encode("utf-8")


	worm = open(title,"r+")
	lines = worm_soup.findAll(text = True)

	worm.truncate()
	for line in lines:
		worm.write(line)
	worm.close()


	p = re.compile("(Next)+")
	
	
	for line in soup.findAll("a"):
		href = p.search(str(line))
		try:
			h = href.group()
			#print line
			worm_url = line.get("href")
			print(worm_url)
			if count < 15:
				call_worm(worm_url)
			else:
				sys.exit()
		except:
			pass

def call_worm(worm_url):
	worm(worm_url)
	

			
worm(start_url)