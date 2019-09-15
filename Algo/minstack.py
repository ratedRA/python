class MinStack:
    def __init__(self):
		self.stack1 = []
		self.stack2 = []
		self.size = 0

    def push(self, x):
        if self.size == 0:
            self.stack2.append(x)
        else:
        	if x<=self.stack2[-1]:
        		self.stack2.append(x)
        self.stack1.append(x)
        self.size+=1


    def pop(self):
    	if len(self.stack1)<=0:
    		return
    	if len(self.stack1)>0 and len(self.stack2)>0 and self.stack1[-1]==self.stack2[-1]:
    		del self.stack2[-1]
    	del self.stack1[-1]
    	self.size-=1


    # @return an integer
    def top(self):
    	if len(self.stack1)==0:
    		return -1
    	else:
    		return self.stack1[-1]


    # @return an integer
    def getMin(self):
    	if len(self.stack1)==0 or len(self.stack2)==0:
    		return -1
    	x = self.stack2[-1:]
    	return self.stack2[-1]

