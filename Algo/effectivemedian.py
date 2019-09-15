import math
import heapq

def insert(p,q,n):
	if len(p)==0:
		heapq.heappush(p,n)
		return
	elif len(q)==0:
		heapq.heappush(q,n)
		return
	else:
		

j = 1
p = []
q = []
while 1:
	n = int(input())

	insert(p,q,n)
	j+=1

	if j == 1:
		print('median is %d'%(n))

	else:
		if j%2==0:
			a = -1*heapq.heappop(p)
			heapq.heappush(p,-1*a)
			b = -1*heapq.heappop(q)
			heapq.heappush(q,-1*b)
			median = (a+b)/2
			median = round(median,1)
		else:
			size1 = len(p)
			size2 = len(q)
			if size1>size2:
				median = -1*heapq.heappop(p)
				heapq.heappush(p,-1*median)
			else:
				median = -1*heapq.heappop(q)
				heapq.heappush(q,-1*median)