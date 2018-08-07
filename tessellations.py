# tessellations.py
from PIL import Image, ImageDraw
import math

length = 100

def draw_triangle(image, x, y, theta):
	theta = -theta * math.pi / 180
	
	draw = ImageDraw.Draw(image)
	draw.line((
		(x, y),
		(x + length * math.cos(theta) / 2, y + length * math.sin(theta) / 4),
		(x + length * math.cos(math.pi / 6 + theta), y + length * math.sin(math.pi / 6 + theta)),
		(x + length * math.cos(theta - math.pi / 6), y + length * math.sin(theta - math.pi / 6)),
		(x + length * math.cos(theta - math.pi / 3) / 2 + length * math.sin(theta) * math.sin(math.pi / 3) / 4, y + length * math.sin(theta - math.pi / 3) / 4 + length * math.cos(math.pi / 6 + theta) * math.sin(math.pi / 3)),
		(x, y)
		), fill = (0, 0, 0), width = 2)
	return(image)

image = Image.new("RGB", (512, 512), (255, 255, 255))

for i in range(1):
	image = draw_triangle(image, 256, 256, 60 * i)
image.show()
