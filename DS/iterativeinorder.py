import math

class Node(object):
	def __init__(self, data):
		self.data = data
		self.leftChild = None
		self.rightChild = None

def itr_in_order(root):
	currentNode = root
	stack = []
	#stack.append(root)
	while True:

		if currentNode is not None:
			stack.append(currentNode)
			currentNode = currentNode.leftChild

		elif stack:
			current = stack.pop()
			print(current.data)

			currentNode = current.rightChild
		else:
			break