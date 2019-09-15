# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def recoverTree(self, A):
	    def inorder(root,m):
        	if root.left:
        		inorder(root.left,m)
        	m.append(root.val)
        	if root.right:
        		inorder(root.right,m)
        	return m
        def recover(root):
        	m = []
        	a = inorder(root, m)
        	pair= []
        	for i in range(0,len(a)-1):
        		if a[i]>a[i+1]:
        			pair.append((a[i],a[i+1]))
        	if len(pair) == 1:
        		return [pair[0][1], pair[0][0]]
        	else:
        		f = max(pair[0])
        		s = min(pair[1])
        		return [s,f]
        return recover(A)
        