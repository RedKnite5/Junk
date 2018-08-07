#  socket_learning_client.py

import socket
 
 
TCP_IP = '142.254.109.186'
TCP_PORT = 5556
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()
 
print("received data:", data)