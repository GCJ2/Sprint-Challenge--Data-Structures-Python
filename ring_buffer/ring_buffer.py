from doubly_linked_list import DoublyLinkedList


class RingBuffer:
	def __init__(self, capacity):
		self.capacity = capacity
		self.current = None
		self.storage = DoublyLinkedList()

	def append(self, item):
		if self.storage.length == 0:                # If storage is empty
			self.storage.add_to_head(item)          # Set passed in item to head
			self.current = self.storage.head        # Set current item to head

		elif self.storage.length < self.capacity:   # If storage is not at capacity
			self.storage.add_to_tail(item)          # Add item passed in to tail
			self.current = self.storage.tail        # Set current item to tail

		elif self.current is self.storage.tail:     # If current item is tail
			self.storage.remove_from_head()         # Remove item at head
			self.storage.add_to_head(item)          # Set passed in item as head
			self.current = self.storage.head        # Set current item as head node

		else:                                       # Otherwise
			self.current.insert_after(item)         # Insert item after current item
			self.storage.length += 1                # Increase size by 1
			self.current = self.current.next        # Set current to item after current
			self.storage.delete(self.current.next)  # Delete item after new current

	def get(self):
		# Note:  This is the only [] allowed
		list_buffer_contents = []

		# TODO: Your code here\
		current_node = self.storage.head                        # Set current node to head
		while current_node is not None:                         # While there is a current node
			list_buffer_contents.append(current_node.value)     # Add the value of the node to the []
			current_node = current_node.next                    # Move on to the next node until None

		return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
	def __init__(self, capacity):
		pass

	def append(self, item):
		pass

	def get(self):
		pass
