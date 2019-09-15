from collections import deque

a = int(input())
q = deque()
q.append(1)
q.append(2)
q.append(3)
front = 0
while len(q)<=a:
	x1,x2,x3 = 10*q[front]+1,10*q[front]+2,10*q[front]+3
	q.append(x1)
	q.append(x2)
	q.append(x3)
	front+=1
print(q[a-1])
