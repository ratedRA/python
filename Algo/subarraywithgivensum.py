import math

a = list(map(int, input().split()))
b = int(input())

i,j = 0,0
sum1 = a[0]
n = len(a)
while i<n and j<n:
	if sum1<b:
		j+=1
		if j>=n:
			print(-1)
			break
		sum1+=a[j]
	elif sum1>b:
		i+=1
		if i>=n:
			print(-1)
			break
		sum1-=a[i-1]
	else:
		print(a[i:j+1])
		break
	#print(sum1)