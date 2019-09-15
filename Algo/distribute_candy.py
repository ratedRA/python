from heapq import heapify, heappush, heappop
from collections import defaultdict

a = list(map(int, input().split()))
#a.sort()

sum1 = defaultdict(lambda:1)
q = []
for i in range(len(a)):
	heappush(q, (a[i],i))
res = 0
while q:
	num, i = heappop(q)
	#print(num,i)
	if i-1>=0 and (i+1)<len(a):
		if a[i-1]<a[i] and a[i]>a[i+1]:
			sum1[(a[i],i)] = max(sum1[(a[i-1],i-1)], sum1[(a[i+1],i+1)])+1
		elif a[i-1]<a[i]:
			sum1[(a[i],i)] = sum1[(a[i-1],i-1)]+1
		elif a[i+1]<a[i]:
			sum1[(a[i],i)] = sum1[(a[i+1],i+1)]+1
	elif i-1>=0:
		if a[i-1]<a[i]:
			sum1[(a[i],i)] = sum1[(a[i-1],i-1)]+1
			#print('yes')
		#print(i)
	elif i+1<len(a):
		if a[i+1]<a[i]:
			sum1[(a[i],i)] = sum1[(a[i+1],i+1)]+1

for i in range(len(a)):
	#print(sum1[(a[i],i)])
	res+= sum1[(a[i],i)]
print(res)