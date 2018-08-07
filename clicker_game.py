import mod,pickle,sys
from datetime import datetime

# python clicker_game.py

buyable = {
"Oven":["Oven","click_val+=1",10,"makes 1 cookie per second"]
}




def start():
	global click_val,save,upgrades,cookies
	click_val = 1
	load = mod.lower_input("Load previous save?")
	if load in ("yes","load"):
		try:
			save = pickle.load(open("clicker_file.txt","rb"))
			cookies = save[0]
			upgrades = save[1]
		except:
			print("No save file found.")
			cookies = 0
			upgrades = {}
	else:
		print("test")
		cookies = 0
		upgrades = {}
	instructions()
	base()

	
	
def instructions():
	global click_val,save,upgrades,cookies
	print("type \"c\" or \"cookie\" to get cookies!")
	print("type \"help\" too see this again.")
	print("type \"upgrades\" to see and buy upgrades.")
	print("type \"save\" to save.")
	print("type \"quit\" to exit.")
	return()


def base():
	global click_val,save,upgrades,cookies
	print("You have ",cookies,"cookies!")
	input = mod.lower_input()
	if input in ("quit","exit"):
		q = mod.lower_input("Do you want to save?")
		if q in ("y","yes","save"):
			save = [cookies,upgrades]
			pickle.dump(save,open("clicker_file.txt","wb"))
			sys.exit()
		else:
			sys.exit()
	elif input in ("c","cookie"):
		cookies += click_val
	elif input in ("help","instructions"):
		instructions()
	elif input in ("save"):
		save = [cookies,upgrades]
		pickle.dump(save,open("clicker_file.txt","wb"))
	elif input in ("upgrades"):
		upgrade_menu()
	
	base()
		
def upgrade_menu():
	print("Upgrade Menu")
	input = mod.lower_input()
	if input in ("old","purchased","purchased upgrades","bought"):
		if len(upgrades) == 0:
			print("No upgrades purchased")
		for i in upgrades:
			print(i)
		upgrade_menu()
	elif input in ("new","unpurchased","purchasable","purchaseable upgrades","for sale","buyable"):
		if len(buyable) == 0:
			print("No buyable items")
		for i,list in buyable.items():
			print(i," Cost:",list[2]," ",list[3])
		upgrade_menu()
	elif input in buyable:
		buy(input)
	elif input in ("quit","exit"):
		return()
	else:
		print("That is not an option.")
		upgrade_menu()
	return()

def buy(upgrade):
	print("buy")
	if upgrade in upgrades:
		upgrades[mod.devar(upgrade)][4] += 1
	else:
		upgrades[mod.devar(upgrade[0])] = upgrade
	eval(upgrade[1])
	cookies -= upgrade[2]
	print(upgrade[0]," bought!")
	return()





start()