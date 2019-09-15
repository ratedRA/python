import math

def gcd(a,b):
	x1 = max(a,b)
	x2 = min(a,b)

	if x1%x2==0:
		return x2
	else:
		return gcd(x1%x2, x2)

def factor(n, b):
	x = n//2
	if gcd(n,b)==1:
		return n
	max1 = -(math.inf)
	for i in range(x, 1, -1):
		if n%i!=0:
			continue
		else:
			factor1 = i
			factor2 = n//i
			x1 = gcd(factor1,b)
			if x1==1:
				return factor1
	return 1

def efficient_factor(n, b):
	while gcd(n,b)!=1:
		n = n//gcd(n,b)
	return n


a,b = map(int, input().split())
res = efficient_factor(a,b)
print(res)
