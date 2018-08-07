import urllib.request, urllib.error, urllib.parse, sys, re
from bs4 import BeautifulSoup as BSoup
# python webscraping3.py

url = "https://parahumans.wordpress.com/2011/06/14/gestation-1-2/"

page = urllib.request.urlopen(url)
soup = BSoup(page, "html.parser")

print(soup)