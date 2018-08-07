#  graph_class.py


class connection(object):
	def __init__(self, st_node, end_node, ty):
		"""Create a connection between two nodes."""
		
		if isinstance(st_node, node):
			self.start_node = str(st_node)
		else:
			self.start_node = st_node
		
		if isinstance(end_node, node):
			self.end_node = str(end_node)
		else:
			self.end_node = end_node
		
		self.con_type = ty
	
	def __eq__(self, other_connection):
		"""Test if two connections are the same."""
		
		if other_connection.con_type != self.con_type:
			return(False)
		if other_connection.start_node != self.start_node:
			return(False)
		if other_connection.end_node != self.end_node:
			return(False)
		
		return(True)
		








class node(object):
	def __init__(self, graph, id):
		self.connections = set()
		self.graph = graph
		self.id = str(id)
	
	def __repr__(self):
		return(self.id.replace(" ", "_"))
		
	def __str__(self):
		return(self.id)
		
	def add_half_connection(self, con_node):
		if con_node not in self.graph.get_all_nodes(
		) and con_node not in self.graph.get_all_nodes().values():
			print("That node does not exist.")
			raise ValueError
		
		if isinstance(con_node, node):
			self.connections.add(connection(self, con_node, "one way"))
		else:
			self.connections.add(self.graph.get_node(con_node))
		
	def add_connection(self, con_node):
		if con_node not in self.graph.get_all_nodes(
		) and con_node not in self.graph.get_all_nodes().values():
			print("That node does not exist.")
			raise ValueError
	
		self.add_half_connection(con_node)
		if isinstance(con_node, node):
			con_node.add_half_connection(self)
		else:
			self.graph.get_node(con_node).add_half_connection(self)
	
	def get_connections(self):
		if self.connections == set():
			return(None)
		else:
			return(self.connections)


class graph(object):
	
	def __init__(self):
		self.nodes = {}
		
	def get_node(self, id):
		return(self.nodes[id])
		
	def get_all_nodes(self):
		return(self.nodes)
	
	def add_node(self, id = None):
		if id is None:
			id = len(self.nodes)
			
		if isinstance(id, node):
			self.nodes[id.id] = id
			id.graph = self
		else: 
			self.nodes[str(id)] = node(self, str(id))
			return(self.nodes[str(id)])
			
	def __add__(self, second_graph):
		new_graph = graph()
		for i in self.nodes:
			new_graph.add_node(self.nodes[i])
		second_graph_nodes = second_graph.get_all_nodes()
		for i in second_graph_nodes:
			new_graph.add_node(second_graph_nodes[i])
		return(new_graph)


family = graph()


me = family.add_node("Max")
dad = family.add_node("Dave")
mom = family.add_node("Sandy")
connie = family.add_node("Connie")
tim = family.add_node("Tim")
wendy = family.add_node("Wendy")
elise = family.add_node("Elise")
aunt_susan = family.add_node("Susan")
penny = family.add_node("Penny")
grandma = family.add_node("grandma")

me.add_connection(dad)
me.add_connection("Sandy")
dad.add_connection("Sandy")
mom.add_connection("Connie")
connie.add_connection("Tim")
connie.add_connection(wendy)
connie.add_connection(elise)
tim.add_connection(wendy)
tim.add_connection(elise)
wendy.add_connection("Elise")
dad.add_connection("Susan")
penny.add_connection(dad)
penny.add_connection("Susan")
grandma.add_connection(mom)
grandma.add_connection(connie)


inlaws = graph()
my_wife = inlaws.add_node("Sam")
sis_inlaw = inlaws.add_node("Sarah")
my_wife.add_connection("Sarah")

new_fam = family + inlaws

my_wife.add_connection(me)




mem = new_fam.get_all_nodes()

for i in mem:
	print(i, mem[i].get_connections())










