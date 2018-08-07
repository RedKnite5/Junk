from getpass import getuser
from bs4 import BeautifulSoup
import requests
#  python stuff.py


url = "https://10minutemail.com/10MinuteMail/index.html?dswid=6047"

r = requests.get(url)
soup = BeautifulSoup(r.text)

file = open("10minmail.txt","w+")
file.write(str(soup))
file.close()






user = getuser()
print(user)
