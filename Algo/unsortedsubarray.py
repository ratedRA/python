import math

def find_indices(a):
	s = 0
	e = len(a)-1

	for s in range(len(a)-1):
		if a[s]>a[s+1]:
			break

	if sorted(a)==a:
		return -1,-1

	while e>0:
		if a[e]<a[e-1]:
			break
		e-=1
	max1 = a[s]
	min1 = a[s]
	for i in range(s+1, e+1):
		if a[i]<min1:
			min1=a[i]
		if a[i]>max1:
			max1 = a[i]

	for i in range(s):
		if a[i]>min1:
			s = i
			break

	i = len(a)-1
	while i>=e+1:
		if a[i]<max1:
			e = i
			break
		i-=1

	return s,e

a = list(map(int, input().split()))
i,j = find_indices(a)
print(i,j)
