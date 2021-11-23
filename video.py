#  video.py

import time

import cv2, math
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc, VideoCapture


def grass(frame):
	h, w, _ = frame.shape
	green = (0, 99, 49)
	
	poly = [(0, h - 100), (0, h - 80)]
	dir = True
	x = 0
	y = h - 80
	while x <= width:
		x+=10
		if dir:
			y+=10
		else:
			y-=10
		dir = not dir

		poly.append((x, y))

	poly.extend(((width, h - 90), (width, h - 100), (0, h - 100)))
	
	pts = np.array(poly, np.int32)
	cv2.fillPoly(frame, [pts], green)


def person(frame, loc):
	cv2.line(frame, (loc[0], loc[1] + 100), (loc[0], loc[1] - 100), (0, 0, 0), 1)
	#cv2.line(frame, (loc[0], loc[1] + 100), (
	cv2.circle(frame, (loc[0], loc[1] - 150), 50, (0, 0, 0), 1)


def terrain(frame):
	cv2.rectangle(frame, (0, 0), (width, height), (255, 100, 100), -1)
	cv2.rectangle(frame, (0, frame.shape[0] - 100), (width, height), (19,69,139), -1)


'''
def dist_proto(y, x, z):
	#print("y: ", y)
	#print("x: ", x)
	#print("z: ", z)
	
	if z > 0:
		return 0
	
	return int(math.sin(((x*x+y*y)*.5)/9)*255)
'''




width = 600
height = 400
FPS = 2
seconds = 5

fourcc = VideoWriter_fourcc(*'MP42')
video = VideoWriter('./noise.avi', fourcc, float(FPS), (width, height))

#dist = np.vectorize(dist_proto)

for i in range(0, FPS * seconds, 2):
	
	frame = np.zeros((height, width, 3), dtype=np.uint8)
	#frame = np.array(np.fromfunction(dist, (height, width, 3), dtype=np.uint8))
	print(frame.shape)
	terrain(frame)
	grass(frame)
	person(frame, (500, 250))

	
	video.write(frame)
video.release()


video = VideoCapture("noise.avi")
while video.isOpened():
	ret, frame = video.read()
	
	if not ret:
		break

	cv2.imshow("frame", frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
	time.sleep(5)

video.release()
cv2.destroyAllWindows()

