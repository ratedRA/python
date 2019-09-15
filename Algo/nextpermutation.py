import math
from collections import defaultdict
import copy

def next_permu(l):

	l.reverse()
	flag = 0
	#print(l)
	for i in range(1,len(l)):
		if l[i-1]>l[i]:
			flag = 1
			z = copy.copy(l[0:i])
			z.sort()
			#print(z)
			for k in z:
				if l[i]<k:
					min1 = k
					break
			#print(min1)
			minIndex = l.index(min1)
			l[i], l[minIndex] = l[minIndex], l[i]
			#print(min1)
			x = l[0:i]
			#print(x)
			x.sort()
			y = l[i:len(l)]
			y.reverse()
			y.extend(x)
			break
	if flag==0:
		return -1
	else:
		return y


a = list(map(int, input().split()))
res = next_permu(a)
#res.reverse()
print(res)