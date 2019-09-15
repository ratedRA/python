import math

class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def height(root):

	if not root:
		return 0
	return max(height(root.left), height(root.right))+1

def is_balanced(root):

	if  not root:
		return True

	lh = height(root.left)
	rh = height(root.right)

	if (abs(lh-rh)<=1 and is_balanced(root.left) is True and is_balanced(root.right) is True):
		return True

	return False
	