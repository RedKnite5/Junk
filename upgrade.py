#!/usr/bin/env python3

# list of used libraries

# mod.py


if __name__ == "__main__":
	import importlib
	import os

	import pkg_resources
	from subprocess import run

	run(["python", "-m", "pip", "install", "--upgrade", "pip", "--user"])

	packages = [dist.project_name for dist in pkg_resources.working_set]
	for p in packages:
		try:
			run(["python", "-m", "pip", "install", "--upgrade", p, "--user"])
		except Exception:
			pass

	libs = ["sympy", "hashlib", "time", "tkinter", "tensorflow",
        "cx_Freeze", "urllib.request", "numpy", "PIL", "pydub", "statistics",
		"threading", "webbrowser", "email", "selenium", "cmath",
		"bs4", "platform", "pylab", "numba", "unittest", "keras",
		"warnings", "scrapy", "nltk", "pandas", "matplotlib", "boto3",
		"pygame", "pyglet", "keyboard", "plotly", "sqlalchemy", "twisted",
		"decimal", "collections", "doctest", "aiohttp", "docopt", "regex",
        "curses", "flask", "cv2", "networkx", "rope", "wily",
        "coverage", "pycodestyle", "pycurl", "savepagenow",
		"antlr4-python3-runtime", "mypy", "PyPDF2", "django", "pyautogui",]

	modules_list = {}

	if os.name == "nt":
		libs.extend(("winsound",))
		libs.extend(("mahotas", "appJar"))

	if os.name == "posix":
		libs.extend(("enchant",))

	failed_imports = []
	for i in libs:
		try:
			modules_list[i] = importlib.import_module(i)
		except ModuleNotFoundError:
			failed_imports.append(i)
			print("Could not import %s" % i)


		# import graphics			 # doesn't work on either
	print(failed_imports)

	failed_installs = []
	for i in failed_imports:
		try:
			if i == "curses":
				pro = run(["python", "-m", "pip", "install", "windows-curses", "--user"])
			elif i == "PIL":
				pro = run(["python", "-m", "pip", "install", "pillow", "--user"])
			elif i == "cv2":
				pro = run(["python", "-m", "pip", "install", "opencv-python", "--user"])
			else:
				pro = run(["python", "-m", "pip", "install", i, "--user"])
			
			if pro.returncode != 0:
				failed_installs.append(i)
		except Exception:
			failed_installs.append(i)

	print("Done")
	print("Could not install: " + str(failed_installs))
	# ['tensorflow', 'keras']

r'''
list libraries: help("modules")
'''

def lower_input(prompt=""):
	print(prompt)
	return(input().strip().lower())


def devar(x=None):
	return(x)
