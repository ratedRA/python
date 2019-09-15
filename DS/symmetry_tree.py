class Solution:
	# @param A : root node of tree
	# @return an integer
	def isSymmetric(self, A):
	    def symmetry(root1, root2):
        	if root1 is None and root2 is None:
        		return 1
            if root1 is not None and root2 is not None:
            	if (root1.val == root2.val):
            		return (symmetry(root1.left, root2.right) and symmetry(root1.right, root2.left))
        
        	return 0
        
        return symmetry(A.left,A.right)
