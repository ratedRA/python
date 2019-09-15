import math

def segregate(a):
	j = 0
	for i in range(len(a)):
		if a[i]<=0:
			a[i],a[j] = a[j], a[i]
			j+=1
	return j

def find_missing(l):
	print(len(l))
	for i in range(len(l)):
		if abs(l[i])-1 < len(l) and l[abs(l[i])-1]>0:
			l[abs(l[i])-1] = -1*l[abs(l[i])-1]
	print(l)
	for i in range(len(l)):
		if l[i]>0:
			return i+1

	return len(l)+1



a = list(map(int, input().split()))
shift = segregate(a)
res  = find_missing(a[shift:])
print(res)