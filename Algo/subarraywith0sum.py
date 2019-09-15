import math
from collections import defaultdict

a = list(map(int, input().split())):
presum = [0]*len(a)
presum[0] = a[0]
d = defaultdict(lambda:0)
d[presum[0]] += 1
if presum[0]==0:
	print('yes')
for i in range(1, len(a)):
	presum[i] += presum[i-1]+a[i]
	d[presum[i]] += 1
	if presum[i]==0 or d[presum[i]]>=1:
		print('yes')
