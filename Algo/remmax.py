import math

t = int(input())
while t>0:
	n = int(input())
	max1 = -(math.inf)

	for i in range(1,n+1):
		x = i
		x = str(i)
		y = x
		x = x[::-1]
		x = int(x)
		if x>max1:
			max1 = x
			res = y
	print(res)
	t-=1