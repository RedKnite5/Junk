# list of used libraries

# mod.py


if __name__ == "__main__":
	import importlib
	import os

	import pkg_resources
	from subprocess import run

	packages = [dist.project_name for dist in pkg_resources.working_set]
	run("pip3 install --upgrade " + ' '.join(packages), shell=True)

	libs = ["sys", "math", "random", "pickle", "sympy", "hashlib",
		"time", "tkinter", "itertools", "tensorflow", "cx_Freeze",
		"datetime", "timeit", "urllib.request", "numpy",
		"_thread", "string", "colorsys", "PIL", "pydub", "statistics",
		"threading", "re", "webbrowser", "email", "selenium", "cmath",
		"bs4", "platform", "pylab", "numba", "unittest", "keras",
		"warnings", "scrapy", "nltk", "pandas", "matplotlib", "boto3",
		"gensim", "pygame", "pyglet", "seaborn", "keyboard",
		"envelopes", "arrow", "plotly", "sqlalchemy", "twisted",
		"inspect", "decimal", "collections", "doctest", "pip",
		"subprocess", "os", "importlib", "aiohttp", "docopt",
		"regex"]

	modules_list = {}

	if os.name == "nt":
		libs.extend(("winsound",))
		libs.extend(("mahotas", "appJar"))

	if os.name == "posix":
		libs.extend(("curses",))
		libs.extend(("enchant",))

	failed_imports = []
	for i in libs:
		try:
			modules_list[i] = importlib.import_module(i)
		except ModuleNotFoundError:
			failed_imports.append(i)
			print("Could not import %s" % i)
	
	try:
		import cv2
	except:
		print("Could not import cv2")
		run("pip3 install opencv-python", shell = True)
		

	# import graphics             # doesn't work on either
print(failed_imports)

for i in failed_imports:
	try:
		run("pip3 install " + i, shell = True)
	except:
		pass

print("Done")
r'''
cd C:\Users\Max\Documents\Python\Calculator
cd C:\Users\Max\Dropbox\Python

list libraries: help("modules")
'''

def lower_input(prompt=""):
	print(prompt)
	return(input().strip().lower())


def devar(x=None):
	return(x)
