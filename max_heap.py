# Class for max heap objects. These objects are used
# to create a max heap of hash key pairs.
import sys


class MaxHeap:
	# Constructor.
	def __init__(self, max_size):
		self.max_size = max_size
		self.size = 0
		self.heap = [0] * (self.max_size + 1)
		self.heap[0] = sys.maxsize
		self.front = 1

	# Return index of parent node of node positioned at parameter index.
	def get_parent_index(self, node_index):
		return node_index // 2

	# Return node index of right child of node positioned at parameter index.
	def get_right_child_index(self, node_index):
		return (2 * node_index) + 1

	# Return node index of left child of node positioned at parameter index.
	def get_left_child_index(self, node_index):
		return 2 * node_index

	# Return true if node positioned at parameter index is a leaf, else return false.
	def is_leaf(self, node_index):
		if (self.size // 2) <= node_index <= self.size:
			return True
		else:
			return False

	# Swap position of two nodes positioned at two respective parameter indices.
	def swap_nodes(self, node_index_a, node_index_b):
		self.heap[node_index_a], self.heap[node_index_b] = self.heap[node_index_b], self.heap[node_index_a]

	# Heapify the node positioned at parameter index.
	def heapify_node(self, node_index):
		# If node is not a leaf, enter statement.
		if not self.is_leaf(node_index):
			# If node is smaller than either of its children, enter statement.
			if (self.heap[node_index] < self.heap[self.get_left_child_index(node_index)] or
					self.heap[node_index] < self.heap[self.get_right_child_index(node_index)]):

				# If left child node is greater than the right child node,
				# swap node with left child node, then heapify new left child node (old node in new position).
				if self.heap[self.get_left_child_index(node_index)] > self.heap[self.get_right_child_index(node_index)]:
					self.swap_nodes(node_index, self.get_left_child_index(node_index))
					self.heapify_node(self.get_left_child_index(node_index))
				# Else right child node is greater than the left child node,
				# swap node with right child node, then heapify new right child node (old node in new position).
				else:
					self.swap_nodes(node_index, self.get_right_child_index(node_index))
					self.heapify_node(self.get_right_child_index(node_index))

	# Insert new node into heap.
	def insert_node(self, node):
		# If heap is full, do nothing and return.
		if self.size >= self.max_size:
			return
		self.size += 1
		new_node_index = self.size
		self.heap[new_node_index] = node

		# While new node is larger than its parent,
		# swap new node with its parent until it is smaller than its parent.
		while self.heap[new_node_index] > self.heap[self.get_parent_index(new_node_index)]:
			self.swap_nodes(new_node_index, self.get_parent_index(new_node_index))
			new_node_index = self.get_parent_index(new_node_index)

	# Pop and return the maximum node from the heap.
	def pop_max_node(self):
		popped_max_node = self.heap[self.front]
		self.heap[self.front] = self.heap[self.size]
		self.size -= 1
		self.heapify_node(self.front)
		return popped_max_node

	# Display contents of heap in order.
	def display_heap(self):
		print("Max Heap Contents:")
		for i in range(1, (self.size // 2) + 1):
			print("Node: " + str(self.heap[i]) + ", " +
				  " Left Child: " + str(self.heap[self.get_left_child_index(i)]) + ", " +
				  " Right Child: " + str(self.heap[self.get_right_child_index(i)]))


# Driver code for testing class.
if __name__ == "__main__":
	heap = MaxHeap(5)
	heap.insert_node(1)
	heap.insert_node(4)
	heap.insert_node(2)
	heap.insert_node(5)
	heap.insert_node(3)
	heap.display_heap()