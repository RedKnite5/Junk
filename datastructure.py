# datastructure.py

class Graph(object):
	def __init__(self, nodes=None):
		self.nodes = []
		self.connections = []
		
		if type(nodes) == dict:
			for i in nodes.items():
				self.nodes.extend(i)
				self.connections.append(i)
		elif type(nodes) == tuple:
			if type(nodes[0]) == tuple:
				for i in nodes:
					self.nodes.extend(i)
					self.connections.append(i)
			else:
				self.nodes.extend(nodes)

		self.nodes = list(set(self.nodes))
		
	def add_node(self, node):
		self.nodes.append(node)
		
	def add_nodes(self, nodes):
		self.nodes.extend(nodes)
	
	def merge_graphs(self, graph):
		if isinstance(graph, Graph):
			return Graph(self.
		
	def add_connection(self, node1, node2):
		if node1 in self.nodes and node2 in self.nodes:
			self.connections.append((node1, node2))
		else:
			raise IndexError("Nodes not in graph")
	
	def get_connections(self, node=None):
		if node == None:
			return tuple(self.connections)
		else:
			return tuple(i for i in self.connections if node in i)

g = Graph()

g.add_node("me")
g.add_node("mom")
g.add_connection("me", "mom")
a = g.get_connections("me")

print(a)

