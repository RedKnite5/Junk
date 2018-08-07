from twisted.internet.protocol import Protocol
# python test_twisted_server.py

class echo(Protocol):
	
	def __init__(self, factory):
		self.factory = factory
	
	def connectionMade(self):
		self.transport.write("connection made\r\n")
	
	def dataReceived(self, data):
		self.transport.write(data)
		
endpoint = 