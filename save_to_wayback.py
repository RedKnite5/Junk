#!/mnt/c/Users/RedKnite/AppData/Local/Programs/Python/Python38/python.exe
# save_to_wayback.py

import sys
import time
from urllib.parse import urljoin
import bs4
import requests
import savepagenow as save

def is_next_btn(tag):
    try:
        assert ["btn"] == tag["class"]
        assert tag.text == "Next >"
        return True
    except (KeyError, AssertionError) as e:
        return False

def get_next(url):
    page = requests.get(url)

    soup = bs4.BeautifulSoup(page.text, "html.parser")

    btns = soup.find_all(is_next_btn)
    try:
        assert btns[0]["onclick"] == btns[1]["onclick"]
    except IndexError:
        return None
    assert btns[0]["onclick"].startswith("self.location='")

    return urljoin("https://www.fanfiction.net/" ,btns[0]["onclick"][15:][:-1])

url = sys.argv[1]

errors = []

while url:
    try:
        save.capture(url)
    except save.api.WaybackRuntimeError:
        print(f"Error: {url}")

        time.sleep(60)
        print("slept")
        try:
            save.capture(url)
        except save.api.WaybackRuntimeError:
            errors.append(url)
            sys.exit()
        else:
            print(f"Saved: {url}")
    else:
        print(f"Saved: {url}")

    url = get_next(url)