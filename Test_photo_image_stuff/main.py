from PIL import Image
from PIL import ImageOps
from PIL import ImageTk

import module as m



b = m.B()

class A(object):
	
	def __init__(self):
		image = Image.open("gold.png")
		image = image.resize((20, 20))
		type(self).image = ImageTk.PhotoImage(image)


class A_sub(A):
	def __init__(self):
		super().__init__()
		
		image = Image.open("gold.png")
		image = image.resize((200, 200))
		type(self).image = ImageTk.PhotoImage(image)
		
		

a = A_sub()
b.func(a)

print(__file__)