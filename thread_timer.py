
import threading
import time

def foo(*args, **kwargs):
	print("TIME!")

def main():
	t = threading.Timer(3, foo)
	t.start()
	while True:
		print("going")
		time.sleep(1)

main()