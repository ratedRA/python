from heapq import heappush, heappop
import heapq

a = list(map(int, input().split()))

heapq.heapify(a)
res = 0
while a:
	min1 = heappop(a)
	if len(a)==0:
		print(res)
		break
	min2 = heappop(a)

	sum1 = min1+min2
	res += sum1
	heappush(a, sum1)
	#print(a)