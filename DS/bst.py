import math

class Node(object):

	def __init__(self, data):
		self.data = data
		self.leftChild = None
		self.rightChild = None

class Bst(object):

	def __init__(self):
		self.root = None

	def insert(self, data):

		if not self.root:
			self.root = Node(data)
		else:
			self.insert2(data, self.root)

	def insert2(self, data, node):

		if not node:
			return 

		if data < node.data:
			if node.leftChild:
				self.insert2(data, node.leftChild)
			else:
				node.leftChild = Node(data)

		elif data > node.data:
			if node.rightChild:
				self.insert2(data, node.rightChild)
			else:
				node.rightChild = Node(data)

	def traverse(self):

		if self.root == None:
			return 'tree is empty'

		else:
			print("preorder traversal is:")
			self.preorder(self.root)
			print()
			print("inorder traversal is:")
			self.inorder(self.root)
			print()

	def preorder(self, node):

		print(node.data, end = " ")
		if node.leftChild:
			self.preorder(node.leftChild)
		if node.rightChild:
			self.preorder(node.rightChild)

	def inorder(self, node):

		if node.leftChild:
			self.inorder(node.leftChild)
		print(node.data, end = " ")
		if node.rightChild:
			self.inorder(node.rightChild)

	def height(self):
		tree_height = self.max_depth(self.root)
		return tree_height

	def max_depth(self, node):
		if not node:
			return 0;
		else:
			lheight = self.max_depth(node.leftChild)
			rheight = self.max_depth(node.rightChild)

			return max(lheight+1, rheight+1)

	def diameter(self):
		return self.cal_diameter(self, self.root):

	def cal_diameter(self, node):
		if not node:
			return None
		else:
			lheight = self.height(node.leftChild)
			rheight = self.height(node.rightChild)

			ldiameter = self.cal_diameter(node.leftChild)
			rdiameter = self.cal_diameter(node.rightChild)

			return max(max(ldiameter,rdiameter), lheight+rheight+1)

b = Bst()
print("insert 5 element into bst in a row with spaces")
a = input().split()
for i in a:
	print(i)
	b.insert(int(i))

b.traverse()
print('height of the tree is {0}'.format(b.height()))