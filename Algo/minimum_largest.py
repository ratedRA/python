from heapq import heappush, heappop
import copy

a = list(map(int, input().split()))
#a.sort()
b = int(input())
c = copy.copy(a)
q = []
#heapq.heapify(a)
for i in range(len(a)):
	heappush(q, (c[i]+a[i],i))
res = []
while b>0:
	val, ind = heappop(q)
	c[ind] += a[ind]
	b-=1
	heappush(q, (c[ind]+a[ind], ind))
	print(c)
	

print(max(c))
