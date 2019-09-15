import math

a = list(map(int, input().split()))
k = int(input())

l = min(a)
h = max(a)

while l<=h:
	m = (l+h)//2
	x1, x2 = 0, 0
	for i in a:
		if i<m:
			x1+=1
		else:
			x2+=1

	if x1<(k-1):
		l = m+1
	elif x1>(k-1):
		h = m-1

	else:
		print(m)
		break

l = min(a)
h = max(a)
n = len(a)

while l<=h:
	m = (l+h)//2
	x1, x2 = 0, 0
	for i in a:
		if i<m:
			x1+=1
		else:
			x2+=1

	if x2<(k-1):
		h = m-1
	elif x2>(k-1):
		l = m+1

	else:
		print(m)
		break



