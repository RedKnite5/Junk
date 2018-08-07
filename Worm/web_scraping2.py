import urllib2
from bs4 import BeautifulSoup as BSoup

VALID_TAGS = []

wiki = "https://parahumans.wordpress.com/2011/06/11/1-1/"

page = urllib2.urlopen(wiki)

soup = BSoup(page, "html.parser")

soup.prettify().encode("utf-8")


soup.find_all("p")

title = str(soup.title)

worm = open("worm_blender.txt","w+")
worm.write(str(soup))
worm.close()