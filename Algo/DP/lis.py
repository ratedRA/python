import math

a = list(map(int,input('enter the list: ').split()))
lis = [1]*(len(a))
for i in range(1, len(a)):
	for j in range(0, i):
		if a[i] > a[j] and lis[i]<lis[j]+1:
			lis[i] = lis[j]+1

print(max(lis))