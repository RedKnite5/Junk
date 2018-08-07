# -*- coding: utf-8 -*-
import urllib2, sys
from bs4 import BeautifulSoup as BSoup
reload(sys)  
sys.setdefaultencoding('utf8')


wiki = "https://parahumans.wordpress.com/2011/06/11/1-1/"
page = urllib2.urlopen(wiki)
soup = BSoup(page, "html.parser")
soup.prettify().encode("utf-8")

title = str(soup.title.get_text())
title_ = title[0:len(title)-6]
title = title_ + ".txt"

print str(soup.title)

worm = open(title,"w+")
worm.write(str(soup.encode("utf-8")))
worm.close()

aline = 0
worm = open(title,"r+")
d = worm.readlines()
worm.seek(0)
for i in d:
	if "<p style=\"text-align:right;\">" in i or "<p dir=\"ltr\" style=\"text-align:center;\">" in i:
		aline += 1
	if aline == 2 or str(soup.title) in i:
		worm.write(i)
worm.truncate()
worm.close()

tagged = "file:///C:/Users/Max/Documents/Python/Worm/"
tagged += title
tagged_worm = urllib2.urlopen(tagged)
worm_soup = BSoup(tagged_worm, "html.parser")
worm_soup.encode("utf-8")


worm = open(title,"r+")
lines = worm_soup.findAll(text = True)

worm.truncate()
for line in lines:
	worm.write(line)
worm.close()

















