import sys, tkinter
import cmath as c
import random as rand
from tkinter import *

def lower_input(*arg):
	if len(arg) == 1:
		print(arg[0])
	x = input()
	return(x.lower())






def start():
	make_map()
	room()

def make_map():
	for x in range(10):
		for y in range(10):
			map[x][y] = rand.randint(5,100)
	map[0][0] = 1
	
	
	
def room():
	print(place)
	r = map[int(place[0].real)][int(place[0].imag)]
	if r == 1:
		print("A chest contains a rusty sword.")
		weapon[0] = oragin_chest[0]
		print(weapon)
		map[int(place[0].real)][int(place[0].imag)] = 0
		action()
	elif r == 0:
		action()
	elif r > 5:
		enemy_encounter_1_start(r)
		
		
	print("ERROR")

#in development	
def open_a_chest():
	print("There is a chest would you like to open it?")
	open_chest = lower_input()
	if open_chest == "yes":
		""""stuff"""
	elif open_chest == "exit":
		sys.exit()

	
def move():
	print("North, South, East, or West?")
	go = lower_input()
	if go == "north":
		place[0] += 1j
		room()
	elif go == "south":
		place[0] -= 1j
		room()
	elif go == "east":
		place[0] += 1
		room()
	elif go == "west":
		place[0] -= 1
		room()
	elif go == "exit":
		sys.exit()
	else:
		print("ERROR")
		move()
		
		
def action():
	print("What do you do?")
	action_var = lower_input()
	if action_var == "move":
		move()
	elif action_var == "i" or action_var == "inventory":
		open_inventory()
	elif action_var == "exit":
		sys.exit()
	
	
	else:
		print("ERROR")
		action()
	action()
		
	
	
def enemy_encounter_1_start(r):
	gob_stat = [0,0,0,0]
	gob_stat[0] =(rand.randint(10,15))
	gob_stat[1] =(rand.randint(0,5))
	gob_stat[2] =(rand.randint(40,60))
	gob_stat[3] =(rand.randint(0,10))
	enemy_encounter(gob_stat)
	
	
def enemy_encounter(gob_stat):
	print("There is a goblin with %d attack, %d defence, and %d health." %(gob_stat[0], gob_stat[1], gob_stat[2]))
	print("What do you do? Attack? Items? Run?")
	act = lower_input()
	if act == "attack":
		gob_stat[2] -= (stats[0]-gob_stat[1])
		print("You delt %d damage!" %stats[0])
	elif act == "items":
		open_inventory(gob_stat)
	elif act == "run":
		if rand.randint(0,5) == 5:
			print("You couldn't get away.")
		else:
			move()
	elif act == "exit":
		sys.exit()
	else:
		print("ERROR")
		enemy_encounter(gob_stat)
				
	while gob_stat[2] > 0:
		print("The goblin attacked and delt %d damage!" %gob_stat[0])
		stats[2] -= (gob_stat[0] - stats[1])
		print("You have %d health" %stats[2])
		
		print("There is a goblin with %d attack, %d defence, and %d health." %(gob_stat[0], gob_stat[1], gob_stat[2]))
		print("What do you do? Attack? Items? Run?")
		act = lower_input()
		if act == "attack":
			gob_stat[2] -= (stats[0]-gob_stat[1])
			print("You delt %d damage!" %stats[0])
		elif act == "Items":
			inventory(gob_stat)
			enemy_encounter(gob_stat)
		elif act == "run":
			if rand.randint(0,5) == 5:
				print("You couldn't get away.")
			else:
				move()
		elif act == "exit":
			sys.exit()
		else:
			print("ERROR")
			enemy_encounter(gob_stat)
	print("You win!")
	print("You get %d gold!" %gob_stat[3])
	inventory[0] += gob_stat[3]
	map[int(place[0].real)][int(place[0].imag)] = 0
	del gob_stat[:]
	room()
			

			
		
				
def open_inventory(*arg):
	#print inventory
	if len(inventory) != 0:
		for x in range(len(inventory)):
			print(inventory[x])
		use_item = lower_input()
		for x in range(len(inventory)):
			if use_item == "quit i":
				return(arg) #potential problem
			elif use_item == "exit":
				sys.exit()
			elif use_item == inventory[x]:
				use(inventory[x])
				return()
		print("You do not have that item.")
		open_inventory(arg)
	else:
		print("Your inventory is empty.")
		return(arg) #potential problem

def use():
	print("not done yet")

	
	
place = [0 + 0j]
map = []
column = []
stats = [20,0,100]
weapon = ["nothing"]
inventory = [0]
oragin_chest = ["rusty sword"]


for x in range(0,10):
	for y in range(0,10):
		column.append(0)
	map.append(column)
	column = []

	

start()