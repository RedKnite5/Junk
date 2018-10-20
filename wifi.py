# wifi.py

import time

from subprocess import check_output, run, CalledProcessError

from xml.dom.minidom import parse
import xml.etree.ElementTree as ET


ET.register_namespace("", r"http://www.microsoft.com/networking/WLAN/profile/v1")

#  netsh wlan export profile name="SCCS" folder="C:\Users\Max\Documents\" key=clear

name = "san lorenzo"

def init_profile(name):
	tree = ET.parse(r"C:\Users\Max\Documents\Wi-Fi-thames.xml")
	root = tree.getroot()
	root[0].text = name
	root[1][0][1].text = name
	root[1][0][0].text = "".join(list(map(lambda a: hex(ord(a))[2:], name)))
	tree.write(r"C:\Users\Max\Documents\Wi-Fi-profile.xml")


#  root[4][0][1][2].text = "g98m4Rs7"  # password


def gen_pass():
	chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890$@^`,|%;.~()/\{}:?[]=-+_#!"
	for i in chars:
		yield f"g98m4Rs{i}"
		#yield f"GanZAUjy"

def check_connected(name):
	output = check_output("netsh wlan show interfaces")

	while b"authenticating" in output:
		time.sleep(.5)
		output = check_output("netsh wlan show interfaces")

	if b"Profile" not in output:
		return False
	else:
		return True
	
	output = output.split(b"\n")

def connect(password):
	tree = ET.parse(r"C:\Users\Max\Documents\Wi-Fi-profile.xml")
	root = tree.getroot()
	root[4][0][1][2].text = password
	print(f"Trying {password}")
	tree.write(r"C:\Users\Max\Documents\Wi-Fi-profile.xml")
	run(r'netsh wlan add profile filename="C:\Users\Max\Documents\Wi-Fi-profile.xml"')
	run(rf'netsh wlan connect "{name}"')
	time.sleep(.05)
	if check_connected(name):
		return
	else:
		raise ConnectionRefusedError


success = False
try:
	run(rf'netsh wlan connect "{name}"')
	
	if not check_connected(name):
		raise ConnectionRefusedError
	success = True
	
except (CalledProcessError, ConnectionRefusedError) as e:
	init_profile(name)
	for i in gen_pass():
		try:
			connect(i)
			success = True
			break
		except (ConnectionRefusedError, CalledProcessError) as e:
			continue

print(success)
