class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def __init__(self):
		self.start = None
	def mergeTwoLists(self, a, b):
		p, q = a, b
		while (p!=None and q!=None):
			if p.val<q.val:
				if self.start == None:
					self.start = ListNode(p.val)
				else:
					ex = self.start
					while ex.next:
					   ex = ex.next
					ex.next = ListNode(p.val)
				p= p.next
			else:
				if self.start == None:
					self.start = ListNode(q.val)
					
				else:
					ex = self.start
					while ex.next:
						ex = ex.next
					ex.next = ListNode(q.val)
				q = q.next
	
		while p:
			ex = self.start
			while ex.next:
				ex = ex.next
			ex.next = ListNode(p.val)
			p = p.next
		while q:
			ex = self.start
			while ex.next:
				ex = ex.next
			ex.next = ListNode(q.val)
			q = q.next
						
					

				

			
				
			
			

