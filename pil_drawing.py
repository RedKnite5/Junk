# pil_drawing.py

from PIL import Image, ImageDraw
import PIL
import os


def draw_lens(image, orient, point1, point2, width, color=(0, 0,0)):
	draw = ImageDraw.Draw(image)
	
	draw.arc((100, 100, 400, 200),0, 180, fill=color)



image_name = "mess2.jpg"

pic = Image.new("RGB",(512,512),(255,255,255))

draw_lens(pic, 0, 0,0,0)

pic.show()

'''
line_coords = ((100,100),(100,400),(400,400),(100,100))
draw.line(line_coords,fill=(255,0,0),width=20)

draw.arc((312,-200,712,212),start=90,end=270,fill="blue")

draw.ellipse((100,100,200,200),fill="green")

draw.text((200,256),"Python is awesome",fill="orange")

pic.show()


save_dir = os.path.join(os.environ["userprofile"],
"Documents\Python\junk\gen_images",
image_name)

pic.save(save_dir,"JPEG")
'''