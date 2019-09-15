# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        def sum1(root):
        	if  not root:
        		return 0
        	return sum1(root.left)+root.val+sum1(root.right)

        def isSumTree(root):
        
        	if (root==None or (root.left==None and root.right==None)):
        		return 1
        
        	ls = sum1(root.left)
        	rs = sum1(root.right)
        
        	if (root.val == ls+rs and isSumTree(root.left) and isSumTree(root.right)):
        		return 1
        
        	return 0

        return isSumTree(A)