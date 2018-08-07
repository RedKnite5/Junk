# python decorate.py 

def dec(func):
	def wrap():
		print("bor")
		func()
		print("post bor")
		
	return(wrap)
	
def req():
	print("!!!!")
	
req = dec(req)

req()
