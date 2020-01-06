# graph.py



class Graph(object):
	def __init__(self):
		self.connections = {}
	
	def add_connection(self, node1, node2):
		if node1 not in self.connections:
			self.connections[node1] = {node2}
		else:
			self.connections[node1].add(node2)
	



