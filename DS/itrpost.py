import math

class Node(object):
	def __init__(self, data):
		self.data = data
		self.leftChild = None
		self.rightChild = None

def peek(stack):
	if len(stack)>0:
		return stack[-1]
	return None

def itr_in_order(root):
	currentNode = root
	stack = []
	#stack.append(root)
	while True:

		while currentNode:
			if currentNode.rightChild:
				stack.append(currentNode.rightChild)
			stack.append(currentNode)
			currentNode = currentNode.leftChild

		currentNode = stack.pop()

		if (currentNode.rightChild is not None and peek(stack)==currentNode.rightChild):
			stack.pop()
			stack.append(currentNode)
			#stack.append(currentNode.rightChild)
			currentNode = currentNode.rightChild
		else:
			res.append(currentNode.data)
			currentNode = None

		if len(stack)<=0:
			break