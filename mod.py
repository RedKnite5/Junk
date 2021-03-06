# list of used libraries

# mod.py


if __name__ == "__main__":
	import importlib
	import os

	import pkg_resources
	from subprocess import run

	run("python -m pip install --upgrade pip --user", shell=True)

	packages = [dist.project_name for dist in pkg_resources.working_set]
	run("pip3 install --upgrade " + ' '.join(packages) + " --user", shell=True)

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
		"regex", "curses", "flask", "cv2", "networkx", "rope",
		"radon", "wily", "coverage", "pycodestyle"]

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


		# import graphics             # doesn't work on either
	print(failed_imports)

	failed_installs = []
	for i in failed_imports:
		try:
			if i == "curses":
				pro = run("pip3 install windows-curses --user", shell=True)
			elif i == "PIL":
				pro = run("pip3 install pillow --user", shell=True)
			elif i == "cv2":
				pro = run("pip3 install  opencv-python --user", shell=True)
			else:
				pro = run("pip3 install " + i + " --user", shell=True)
			
			if pro.returncode != 0:
				failed_installs.append(i)
		except:
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
