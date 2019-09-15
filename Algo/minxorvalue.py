import math

a = list(map(int, input().split()))
a.sort()
min1 = math.inf
for i in range(0,len(a)-1):
	x = a[i]^a[i+1]
	if x<min1:
		min1 = x
print(min1)