class Node: 
   
    def __init__(self, data): 
        self.data = data 
        self.left = self.right = None
  

def zizagtraversal(root): 
  
    # Base Case 
    if root is None: 
        return

    currentLevel = [] 
    nextLevel = [] 

    ltr = True
  
    # append root to currentlevel stack 
    currentLevel.append(root) 
  
    m = []
    while len(currentLevel) > 0: 

        temp = currentLevel.pop(-1) 

        res.append(temp.data)
  
        if ltr: 

            if temp.left: 
                nextLevel.append(temp.left) 
            if temp.right: 
                nextLevel.append(temp.right) 
        else: 
            # else push right before left 
            if temp.right: 
                nextLevel.append(temp.right) 
            if temp.left: 
                nextLevel.append(temp.left) 
  
        if len(currentLevel) == 0: 

            ltr = not ltr 
            # swapping of stacks 
            m.append(res)
            res = []
            currentLevel, nextLevel = nextLevel, currentLevel 