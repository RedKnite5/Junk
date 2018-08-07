import os, glob
#   python convert_ps_files_broken.py

list = ["daves_painting_using_maxs_painting_program.ps"]

for file in list:
	os.system('convert ' + file + ' ' + "daves_painting.png")
	print(os.system("printf(5)"))