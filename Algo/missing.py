import math

def find_missing(a):
	for i in range(len(a)):
		if (i+1 == a[i]):
			continue
		else:
			a[a[i]-1], a[i] = a[i], a[a[i]-1]


	print(a)

	for i in range(len(a)):
		if i+1 == a[i]:
			continue
		else:
			rep = a[i]
			res = i+1
	return rep, res


a = list(map(int, input().split()))
rep, res = find_missing(a)
print(rep,res)