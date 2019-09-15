# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return a list of list of integers
	def pathSum(self, A, B):
	    import copy
	    def k_sum(root, k, stack):
        	if not root:
        		return []
            #print(stack)
        	if root.left==None and root.right==None:
        		if root.val==k:
        		    x = copy.copy(stack)
        			m.append(x)
        			#print(m)
        	#k-=root.val
        	if root.left:
        		stack.append(root.left.val)
        		k_sum(root.left, k-root.val, stack)
        		stack.pop()
        	if root.right:
        		stack.append(root.right.val)
        		k_sum(root.right, k-root.val, stack)
        		stack.pop()
        	#return m
        stack = []
        global m
        m = []
        if not A:
            return []
        k_sum(A,B,[A.val])
        return m
