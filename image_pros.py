import tkinter as tk
from PIL import Image


#  python image_pros.py

def gen(pix):
	return(pix+1)


pic = Image.open("worm_characters_symbols.png")
pic2 = pic.resize((256,256))


pic2.show()