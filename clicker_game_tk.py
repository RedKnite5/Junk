import mod,pickle,sys,math,time
import tkinter as tk
# python clicker_game_tk.py


def Oven():
	global click_val
	click_val += 1
	if click_val > 1:
		val_msg.set(str(click_val)+" cookies per click!")
	else:
		val_msg.set(str(click_val)+" cookie per click!")
def Automatic_Oven():
	global tm_cookies,tm_msg
	tm_cookies += 1
	if tm_cookies > 1:
		tm_msg.set("You make "+str(tm_cookies)+" cookies per second!")
	else:
		tm_msg.set("You make "+str(tm_cookies)+" cookie per second!")
def Mom():
	global tm_cookies,tm_msg
	tm_cookies += 10
	tm_msg.set("You make "+str(tm_cookies)+" cookies per second!")


buyable = {
"Oven":{"func":Oven,"cost":10,"des":"Makes 1 more cookie per click.","own":0},
"Automatic Oven":{"func":Automatic_Oven,"cost":100,"des":"Makes 1 cookies per second.","own":0},
"Mom":{"func":Mom,"cost":1000,"des":"Makes 10 cookies per second.","own":0}
}


root = tk.Tk()


def start():
	global click_val,save,upgrades,cookies,msg,load_y,load_n
	global tm_cookies,notice_msg,tm_msg,last_time,notice_message
	global tm_message,val_message,val_msg
	click_val = 1
	tm_cookies = 0
	msg = tk.StringVar()
	msg.set("")
	tm_msg = tk.StringVar()
	tm_msg.set("")
	notice_msg = tk.StringVar()
	notice_msg.set("Load previous save?")
	val_msg = tk.StringVar()
	val_msg.set("")
	
	notice_message = tk.Message(root,textvariable=notice_msg,width=180)
	notice_message.pack()
	
	tm_message = tk.Message(root,textvariable=tm_msg,width=180)
	tm_message.pack()
	
	message = tk.Message(root,textvariable=msg,width=180)
	message.pack()
	
	val_message = tk.Message(root,textvariable=val_msg,width=180)
	val_message.pack()
	
	load_y = tk.Button(root,text="Yes",command=load)
	load_y.pack()
	load_n = tk.Button(root,text="No",command=no_load)
	load_n.pack()
	
def add_tm_cookies():
	global cookies,last_time,tm_cookies
	cookies += tm_cookies*(math.floor(time.time())-last_time)
	last_time = math.floor(time.time())
	
	
def load():
	global click_val,save,upgrades,cookies,msg,tm_msg,last_time,notice_message
	try:
		save = pickle.load(open("clicker_file.txt","rb"))
		cookies = save[0]
		upgrades = save[1]
		last_time = save[2]
		for i in upgrades:
			for j in range(upgrades[i]["own"]):
				upgrades[i]["func"]()
	except:
		notice_msg.set("No save file found.")
		notice_message.pack()
		cookies = 0
		upgrades = {}
		last_time = math.floor(time.time())
		
	base()
	
def no_load():
	global click_val,save,upgrades,cookies,last_time
	cookies = 100
	upgrades = {}
	last_time = math.floor(time.time())
	
	base()
	
	
	
def base():
	global click_val,save,upgrades,cookies,msg,load_y,load_n
	global notice_msg,tm_msg,last_time,notice_message,tm_message
	global tm_cookies,cookie,val_msg,upgrade_menu,up_menu
		
	add_tm_cookies()
	load_y.destroy()
	load_n.destroy()
	notice_msg.set("")
	msg.set("You have "+str(cookies)+" cookies!")
	val_msg.set(str(click_val)+" cookie per click!")
	
	save_b = tk.Button(root,text="save",command=save_func)
	save_b.pack()
	cookie=tk.Button(root,text="cookies",command=cookie_click)
	cookie.pack()
	
	upgrade_menu = tk.Menu(root)
	
	up_menu = tk.Menu(upgrade_menu, tearoff=0)
	
	#for loop for all buyable upgrades
	for key in buyable:
		up_menu.add_command(label=(key+": "+str(buyable[key]["des"])+" Cost: "+str(buyable[key]["cost"])),command=lambda k=key: buy(k))
	
	upgrade_menu.add_cascade(label="Upgrades", menu = up_menu)
	root.config(menu=upgrade_menu)
	
def refresh():
	global msg,notice_msg,cookies,click_val
	add_tm_cookies()
	if cookies != 1:
		msg.set("You have "+str(cookies)+" cookies!")
	else:
		msg.set("You have "+str(cookies)+" cookie!")
	notice_msg.set("")
	

def buy(up):
	global click_val,save,upgrades,cookies,tm_cookies,msg,tm_message
	global buyable,upgrade_menu,up_menu
	refresh()
	if cookies >= buyable[up]["cost"]:
		cookies -= buyable[up]["cost"]
		#cost changing in deveopment
		
		#buyable[up]["cost"] = math.floor(buyable[up]["cost"]*1.1)
		#for key in buyable:
		#	up_menu.entryconfigure(1,label=(key+": "+str(buyable[key]["des"])+" Cost: "+str(buyable[key]["cost"])))
		refresh()
		grade=buyable[up]
		if up not in upgrades:
			grade["own"]=1
			upgrades[up]=grade
		else:
			upgrades[up]["own"] += 1
		upgrades[up]["func"]()
	else:
		notice_msg.set("You don't have enought cookies for that.")
		

	
def save_func():
	global save,upgrades,cookies,msg,tm_cookies,last_time,notice_msg
	save=[cookies,upgrades,last_time]
	pickle.dump(save,open("clicker_file.txt","wb"))
	refresh()
	notice_msg.set("Saved!")
	
def cookie_click():
	global cookies,click_val,msg,tm_cookies,last_time
	cookies+=click_val
	refresh()
	
	

	


start()

root.mainloop()