# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
    	self.sortedarr = []

    	self.index = -1

    	self.inorder(root)

    def inorder(self,root):
    	if not root:
    	    return
    	self.inorder(root.left)
    	self.sortedarr.append(root.val)
    	self.inorder(root.right)
        

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return True if self.index+1<len(self.sortedarr) else False

    # @return an integer, the next smallest number
    def next(self):
    	self.index+=1
    	return self.sortedarr[self.index]
        

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),
