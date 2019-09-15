class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def solve(self, root):
        def path(root):
            if not root:
                return []
            stack = []
            
            return (all_path(root, str(root.val), []))
            
        def all_path(root, stack, m):
        	if root.left is None  and root.right is None:
        	    x = stack.split(' ')
        	    y = []
        	    for i in x:
        	        s = ''
        	        for j in i:
        	            s+=j
        	        y.append(s)
        	    m.append(y)
        	    #print(m)
        	if root.left:
        	    m = all_path(root.left, stack+" "+str(root.left.val), m)
        	if root.right:
        	    m = all_path(root.right, stack+" "+str(root.right.val), m)
        	return m

        return path(root)