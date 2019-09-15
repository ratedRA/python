def lca1(root,n1,n2, v):
	if root == None:
		return None
	if root.val==n1:
		v[0] = True
		return root
	if root.val == n2:
		v[1] = True
		return root

	root_left = lca1(root.left, n1,n2,v)
	root_right = lca1(root.right, n1, n2,v)

	if (root_left and root_right):
		return root
	if root_left:
		return root_left
	elif root_right:
		return root_right
	else:
		return None


def find(root, key):
	if not root:
		return False
	if (root.val == key or find(root.left, key) or find(root.right, key)):
		return True
	return False

def findlca(root, n1, n2):
	v = [False, False]
	lca = lca1(root, n1, n2, v)
	if (v[0] and v[1] or v[0] and find(lca, n2) or v[1] and find(lca, n1)):
		return lca
	else:
		return None
				
if findlca(root, n1,n2):
	return findlca(root,n1,n2).val
else:
	return -1