from bs4 import BeautifulSoup
import urllib2, re

url = "https://en.wikipedia.org/wiki/Danielle_Smith"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page,"html.parser")
soup.prettify().encode("utf-8")

for link in soup.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
	if "href" in link.attrs:
		print (link.attrs["href"])
		
