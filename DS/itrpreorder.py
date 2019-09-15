import math

class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def itr_in_order(root):
	currentNode = root
	stack = []
	stack.append(root)

	while stack:
		current = stack.pop()
		print(current.data)

		if current.right:
			stack.append(current.right)
		if current.left:
			stack.append(current.left)