import math

a = list(map(int, input().split()))
b = int(input())
i = 0
n = len(a)
j = n-1
res=0
while i<j:
	sum1 = a[i]+a[j]
	if sum1==b:
		res+=1
		i+=1
		j-=1
	elif sum1>b:
		j-=1
	else:
		i+=1
print(res)