class Node:
	def __init__(self, value=None, next_node=None):
		# the value at this linked list node
		self.value = value
		# reference to the next node in the list
		self.next_node = next_node

	def get_value(self):
		return self.value

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		# set this node's next_node reference to the passed in node
		self.next_node = new_next


class LinkedList:
	def __init__(self):
		# reference to the head of the list
		self.head = None

	def add_to_head(self, value):
		node = Node(value)
		if self.head is not None:
			node.set_next(self.head)

		self.head = node

	def contains(self, value):
		if not self.head:
			return False
		# get a reference to the node we're currently at; update this as we
		# traverse the list
		current = self.head
		# check to see if we're at a valid node
		while current:
			# return True if the current value we're looking at matches our
			# target value
			if current.get_value() == value:
				return True
			# update our current node to the current node's next node
			current = current.get_next()
		# if we've gotten here, then the target node isn't in our list
		return False

	def reverse_list(self, node, prev):
		# You must use recursion for this solution
		# [1, 2, 3]
		if node is not None:                # If there is a node
			next_node = node.next_node      # Instant var with node to be accessed after current node
			print(next_node)
			node.next_node = prev           # Set the next node of current node to previous node
			prev = node                     # Set prev to the node that was passed in
			node = next_node                # Update passed in node with next_node
			self.head = prev                # Set the head to prev
			self.reverse_list(node, prev)   # Run until node is None

		# prev = None                             # Set prev to none as it doesn't exist... yet
		# current = self.head                     # Set current node to self.head
		# while current is not None:              # While there is still a node
		# 	next_node = current.get_next()      # Set the next node to the node after the current node
		# 	current.set_next(prev)              # Set the node after the current node to the previous node
		# 	prev = current                      # Set said previous node to the current node
		# 	current = next_node                 # Set the current node to the next node
		# self.head = prev                        # After loop is done, set the head to prev
