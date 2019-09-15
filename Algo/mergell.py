class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def __init__(self):
    	self.start = None

    def mergeKLists(self, A):
    	from heapq import heapify, heappush, heappop
    	q = []
    	for i in A:
    		heappush(q, (i.val,i))
    	while q:
    		val, ll = heappop(q)
    		if self.start == None:
    			self.start = ListNode(val)
    		else:
    			temp = self.start
    			self.start = ListNode(val)
    			self.start.next = temp
    		if ll.next:
    			heappush(q, (ll.next.val, ll.next))
    	curr = self.start
    	prev = None
    	nextn = None
    	while(curr is not None): 
            nextn = curr.next
            curr.next = prev 
            prev = curr 
            curr = nextn
        self.start = prev 
    	return self.start
