# create_keyframes_new.py
	
detail = 75

key = ""
for i in range(detail + 1):
	gradient = "{background-image: -webkit-gradient(linear, left top, right top, "
	for k in range(detail + 1):
		gradient += "color-stop({percent: <12,f}, hsl({hue}, 100%, 50%)), ".format(percent = k / detail, hue = (i * -360 / detail + k * 1 * 360 / detail) % 360)
	gradient = gradient[:-2] + ");}" 
	key += "{percent: <12,%}{gradient}\n".format(percent = i / detail, gradient = gradient)
print(__file__)
with open("scrollingRainbowTextKeyframe.txt", "w+") as file:
	file.write("@keyframes rainbow {\n")
	file.write(key)
	file.write("}")