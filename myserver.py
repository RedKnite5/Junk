

# myserver.py

import PodSixNet.Channel
import PodSixNet.Server
from time import sleep


class ClientChannel(PodSixNet.Channel.Channel):
	def Network(self, data):
		print(data)
	
	def Close(self):
		self._server.close(self.gameid)


class Server(PodSixNet.Server.Server):
 
	channelClass = ClientChannel
	
	def __init__(self, *args, **kwargs):
		PodSixNet.Server.Server.__init__(self, *args, **kwargs)

	def Connected(self, channel, addr):
		print("new connection:", channel)

	def tick(self):
		self.Pump()



print("STARTING SERVER ON LOCALHOST")
s = Server(localaddr=('localhost', 31425))
while True:
	s.tick()
	sleep(0.01)