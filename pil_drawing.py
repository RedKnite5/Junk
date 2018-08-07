# pil_drawing.py

from PIL import Image, ImageDraw
import os

image_name = "mess2.jpg"

pic = Image.new("RGB",(512,512),(255,255,255))
draw = ImageDraw.Draw(pic)

line_coords = ((100,100),(100,400),(400,400),(100,100))
draw.line(line_coords,fill=(255,0,0),width=20)

draw.arc((312,-200,712,212),start=90,end=270,fill="blue")

draw.ellipse((100,100,200,200),fill="green")

draw.text((200,256),"Python is awesome",fill="orange")

pic.show()

save_dir = os.path.join(os.environ["userprofile"],
"Dropbox\Python\gen_images",
image_name)

pic.save(save_dir,"JPEG")