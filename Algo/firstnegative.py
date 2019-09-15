from collections import deque

def firstneg(a,b):
	q = deque()
	n = len(a)
	res = []
	for i in range(b):
		if a[i]<0:
			q.append(i)

	for i in range(b, n):
		if len(q)!=0:
			res.append(a[q[0]])
		else:
			res.append(0)

		while (len(q)>0 and q[0]<=i-b):
			q.popleft()
		if a[i]<0:
			q.append(i)
	if len(q)!=0:
		res.append(a[q.popleft()])
	else:
		res.append(0)
	return res

a = list(map(int, input().split()))
b = int(input())
print(firstneg(a,b))

