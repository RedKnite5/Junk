#  video.py

import cv2, math
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc, VideoCapture


width = 300
height = 300
FPS = 44
seconds = 15

fourcc = VideoWriter_fourcc(*'MP42')
video = VideoWriter('./noise.avi', fourcc, float(FPS), (width, height))

def make_grass():
	poly = [(0, 500), (0, 510)]
	dir = True
	x = 0
	y = 520
	while x <= width:
		x+=10
		if dir:
			y+=10
		else:
			y-=10
		dir = not dir

		poly.append((x, y))

	poly.append((width, 510))
	poly.append((width, 500))
	poly.append((0, 500))
	return poly


def person(frame, loc):
	cv2.line(frame, (loc[0], loc[1] + 100), (loc[0], loc[1] - 100), (0, 0, 0), 1)
	#cv2.line(frame, (loc[0], loc[1] + 100), (
	cv2.circle(frame, (loc[0], loc[1] - 150), 50, (0, 0, 0), 1)


def terrain(frame):
	cv2.rectangle(frame, (0, 0), (width, height), (255, 100, 100), -1)
	cv2.rectangle(frame, (0, 500), (width, height), (19,69,139), -1)


def dist_proto(y, x, z):
	#print("y: ", y)
	#print("x: ", x)
	#print("z: ", z)
	
	if z > 0:
		return 0
	
	return int(math.sin(((x*x+y*y)*.5)/9)*255)

dist = np.vectorize(dist_proto)

for i in range(0, FPS * seconds, 2):
	
	#frame = np.zeros((height, width, 3), dtype=np.uint8)
	frame = np.array(np.fromfunction(dist, (height, width, 3), dtype=np.uint8))
	print(frame.shape)
	#terrain(frame)
	#poly = make_grass()
	#pts = np.array(poly, np.int32)
	#pts = pts.reshape((-1, 1, 2))
	#cv2.fillPoly(frame, [pts], (0, 99, 49))
	#person(frame, (500, 250))

	
	video.write(frame)
video.release()


video = VideoCapture("noise.avi")
while video.isOpened():
	idk, frame = video.read()
	cv2.imshow("frame", frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

video.release()
cv2.destroyAllWindows()

