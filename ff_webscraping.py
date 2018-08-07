# ff_webscraping.py


import requests
from bs4 import BeautifulSoup
from write_to_file import *

page = requests.get("https://www.fanfiction.net/s/11217421/1/Songs-gone-Unsung")
soup = BeautifulSoup(page.content, "html.parser")


story = soup.find("div", attrs = {'class': ['storytext', 'xcontrast_txt', 'nocopy'], 'id': 'storytext'})
write_to_file(story.get_text(), "test.txt")
