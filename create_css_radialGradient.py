# create_keyframes.py
	
detail = 10

gradient = "background-image: -webkit-radial-gradient(50% 43%, "
for k in range(detail + 1):
	gradient += "hsl({hue}, 100%, 50%), ".format(hue = (k * 2 * 360 / detail) % 360)
gradient = gradient[:-2] + ");"

print(__file__)
with open("C:\\Users\\Max\\Dropbox\\non-python\\create_Rainbow_RadialGradient.txt", "w+") as file:
	file.write(gradient)
