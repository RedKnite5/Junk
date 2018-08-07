# -*- coding: utf-8 -*-
import urllib.request, urllib.error, urllib.parse, sys, re
from bs4 import BeautifulSoup as BSoup

url = "https://en.oxforddictionaries.com/explore/literary-words"
page = urllib.request.urlopen(url)
soup = BSoup(page,"html.parser")
soup = soup.prettify().encode("utf-8")

wordlist = open("wordlist.txt","w+")
wordlist.write(str(soup))
wordlist.close()

filter = re.compile("(strong)+(href)")
