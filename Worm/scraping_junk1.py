# -*- coding: utf-8 -*-
import requests, sys, re, os
import urllib.request
from bs4 import BeautifulSoup as BSoup
# python scraping_junk1.py


#reload(sys)  
#sys.setdefaultencoding('utf8')

max = 10
count = 0
start_url = "https://parahumans.wordpress.com/2013/10/29/30-7/"


def worm_func(url):
	global count
	count += 1
	
	r = requests.get(url)
	page = r.content
	soup = BSoup(page, "html.parser")
	soup.prettify().encode("utf-8")

	title = str(soup.title.get_text())
	title_ = title[:-7]
	title = title_ + ".txt"
	print(title)
	
	filepath = os.path.join("C:\\Users\\Max\\Dropbox\\Python\\Worm",title)
	
	worm = open(filepath,"w+",encoding="utf-8")
	worm.write(str(r.text).replace("\\n","\n"))
	worm.close()

	aline = 0
	worm = open(title,"r+",encoding="utf-8")
	d = worm.readlines()
	worm.seek(0)
	for i in d:
		if "\"Next Chapter\"" in i:
			aline += 1
		if aline == 1 or str(soup.title) in i:
			if "Last Chapter" not in i:
				worm.write(i)
		
	worm.truncate()
	worm.close()

	tagged = "file:///C:/Users/Max/Dropbox/Python/Worm/"
	tagged += title
	tagged_worm = urllib.request.urlopen(tagged)
	worm_soup = BSoup(tagged_worm, "html.parser")
	worm_soup.encode("utf-8")


	worm = open(title,"r+",encoding="utf-8")
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
			if count < max:
				call_worm(worm_url)
			else:
				sys.exit()
		except:
			pass

def call_worm(worm_url):
	worm_func(worm_url)
	

			
worm_func(start_url)