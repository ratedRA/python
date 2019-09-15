class Node(object):
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

def arr_to_bst(a):
	if not arr:
		return None
	n = len(a)
	mid = len(a)//2

	root = Node(a[mid])

	root.left = arr_to_bst(a[:mid])
	root.right = arr_to_bst(a[mid+1:])

	return root