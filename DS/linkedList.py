class Node(object):

	def __init__(self,data):
		self.data = data
		self.nextNode = None

class LL(object):

	def __init__(self):
		self.start = None
		self.size = 0

	def insert_at_beg(self, data):

		if not self.start:
			self.start = Node(data)
		else:
			tempnode = Node(data)
			tempnode.nextNode = self.start	
			self.start = tempnode

	def insert_at_end(self, data):
		if not self.start:
			self.start = Node(data)
		else:
			p = self.start
			while p.nextNode:
				p = p.nextNode

			p.nextNode = Node(data)

	def del_a_data(self, data):
		i = 1
		p = self.start
		flag = 0
		while p.nextNode:
			if p.nextNode.data == data:
				p = p.nextNode.nextNode
				print('DELETED')
				flag = 1
			else:
				p = p.nextNode
		if flag == 0:
			print("data not present")

	def del_at_pos(self, pos):  # to be reviewed

		i = 1
		p, q = self.start, self.start

		if pos == 1: #start node to be deleted
			self.start = p.nextNode
		else:
			while p:
				if i+1 == pos:
					p = q.nextNode.nextNode
					print('DELETED')
					break
				else:
					p = p.nextNode
					q = q.nextNode
					i+=1
	def mid(self):
		p = self.start
        size = 0
        
        while p:
            size+=1
            p = p.nextNode
        #print(size)
        if size==1:
            self.start = self.start.nextNode
        else:
            if size%2==0:
                pos = (size//2)+1
            else:
                pos = (size//2)+1
            
            i = 1
            p = self.start
            while p:
                if i+1 == pos:
                    p.nextNode = p.nextNode.next
                    break
                i+=1
                p = p.next

	def traverse(self):
		if not self.start:
			print("empty list")
		else:
			p = self.start
			while p:
				print(p.data, end = " ")
				p = p.nextNode
			print()

	def detect_loop(self):
		slow = self.start
		fast = self.start

		slow = slow.nextNode
		fast = fast.nextNode.nextNode

		while (fast and fast.next):
			if (slow == fast):
				break
			slow = slow.nextNode
			fast = fast.nextNode.nextNode
		if slow!=fast:
			return None
		slow = self.start
		while(slow!=fast):
			slow = slow.nextNode
			fast = fast.nextNode
		return slow

	def reverse_f_k(self,k):
		return reverse_k(self.root, k)

	def reverse_k(self, p, k):
		curr = p
		prev = None
		nextn = None
		count = 0


		# reverse ll upto first k node
		while (curr!=None and count < k):
			nextn = curr.nextNode
			curr.nextNode = prev
			prev = curr 
			curr = nextn
			count+=1

		if nextn!=None:
			p.next = self.reverse_k(nextn, k)

		return prev

	def remove_duplicate(self):
		p = self.start
		while p:
			if (p.nextNode!=None and p.nextNode.val == p.val):
				while (p.nextNode!=None and p.val == p.nextNode.val):
					p = p.nextNode
				p = p.nextNode
			else:
				new+=p.val




l = LL()
print("insert 5 element into linked list in a row with spaces")
l.insert_at_beg(1)
a = input().split()
for i in a:
	#print(i)
	l.insert_at_end(int(i))

l.traverse()
print('for deletion')
x = int(input("enter a number to delete: "))
l.del_a_data(x)
l.traverse()
y = int(input("enter a pos to delete: "))
l.del_at_pos(y)
l.traverse()