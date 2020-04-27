# Class to create a max heap that stores dictionary items or other
# key value pairs. Designed to be used with WordCountDict() class.


class MaxHeap:
	# Constructor.
	def __init__(self):
		self.size = 0
		self.heap = []
		self.front = 0

	# Return index of parent node of node positioned at parameter index.
	def get_parent_index(self, index):
		return index // 2

	# Return node index of left child of node positioned at parameter index.
	def get_left_child_index(self, index):
		return (2 * index) + 1

	# Return node index of right child of node positioned at parameter index.
	def get_right_child_index(self, index):
		return (2 * index) + 2

	# Return true if node positioned at parameter index is a leaf, else return false.
	def is_leaf(self, index):
		if (self.size // 2) <= index <= self.size:
			return True
		else:
			return False

	# Swap position of two nodes positioned at two respective parameter indices.
	def swap_nodes(self, index_a, index_b):
		self.heap[index_a], self.heap[index_b] = self.heap[index_b], self.heap[index_a]

	# Heapify the node positioned at parameter index.
	def max_heapify_node(self, index):
		left_child_index = self.get_left_child_index(index)
		right_child_index = self.get_right_child_index(index)

		# If node is not a leaf, enter statement.
		if not self.is_leaf(index):
			# If node is smaller than either of its children, enter statement.
			if (self.heap[index][1] < self.heap[left_child_index][1] or
				self.heap[index][1] < self.heap[right_child_index][1]):

				# If left child node is greater than the right child node,
				# swap node with left child node, then heapify new left child node (old node in new position).
				if self.heap[left_child_index][1] > self.heap[right_child_index][1]:
					self.swap_nodes(index, left_child_index)
					self.max_heapify_node(left_child_index)
				# Else right child node is greater than the left child node,
				# swap node with right child node, then heapify new right child node (old node in new position).
				else:
					self.swap_nodes(index, right_child_index)
					self.max_heapify_node(right_child_index)

	# Insert new node into heap.
	def insert_node(self, node):
		if self.size == 0:
			self.heap.append(node)
			self.size += 1
		else:
			self.heap.append(node)
			node_index = self.size
			self.size += 1

			# While new node is larger than its parent,
			# swap new node with its parent until it is smaller than its parent.
			while self.heap[node_index][1] > self.heap[self.get_parent_index(node_index)][1]:
				self.swap_nodes(node_index, self.get_parent_index(node_index))
				node_index = self.get_parent_index(node_index)

	# Insert dictionary into heap.
	def insert_dict(self, word_dict):
		for (key, value) in word_dict.items():
			node = [key, value]
			self.insert_node(node)

	# Pop and return the maximum node from the heap.
	def pop_max_node(self):
		if self.size == 0:
			return
		else:
			max_node = self.heap[self.front]
			self.heap[self.front] = self.heap[self.size - 1]
			self.size -= 1
			self.max_heapify_node(self.front)
			return max_node

	def pop_top_k_words(self, int):
		print("Top " + str(int) + " Repeating Words:")
		for i in range(int):
			max_node = self.pop_max_node()
			print(max_node)

	# Display contents of heap in order.
	def display_heap(self):
		print("Max Heap Contents:")
		for i in range(0, self.size):
			left_child_index = self.get_left_child_index(i)
			right_child_index = self.get_right_child_index(i)

			# Node has both children
			if left_child_index < self.size and right_child_index < self.size:
				print("Node: " + str(self.heap[i]) +
					  " ,Left Child: " + str(self.heap[left_child_index]) +
					  " ,Right Child: " + str(self.heap[right_child_index]))

			# Node has a right child
			if left_child_index >= self.size > right_child_index:
				print("Node: " + str(self.heap[i]) +
					  " ,Left Child: [ None ]" +
					  " ,Right Child: " + str(self.heap[right_child_index]))

			# Node has a left child
			if left_child_index < self.size <= right_child_index:
				print("Node: " + str(self.heap[i]) +
					  " ,Left Child: " + str(self.heap[left_child_index]) +
					  " ,Right Child: [ None ]")

			# Node has no children
			if left_child_index >= self.size and right_child_index >= self.size:
				print("Node: " + str(self.heap[i]) +
					  " ,Left Child: [ None ]" +
					  " ,Right Child: [ None ]")


# Driver code for testing class.
if __name__ == "__main__":
	k = 10
	worddic = {
		"Hello": 250,
		"this": 720,
		"is": 175,
		"a": 233,
		"test": 276,
		"Test": 623,
		"dictionary": 77,
		"Rest": 624,
		"A": 156,
		"program": 499
	}
	heap = MaxHeap()

	for (key, value) in worddic.items():
		pair = [key, value]
		heap.insert_node(pair)

	print("Top " + str(k) + " Repeating Words:")
	for i in range(k):
		topnode = heap.pop_max_node()
		print(str(topnode))
