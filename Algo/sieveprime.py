import math

def seiveofe(n):
	prime = [True for i in range(n+1)]
	p = 2

	while p*p <= n:

		if(prime[p] == True):
			for i in range(p*p, n+1, p):
				prime[i] = False

		p+=1

	return prime

n = int(input('enter the number upto which u want to find the prime numbers:'))
res = seiveofe(n)
for i in range(2, n+1):
	if res[i] == True:
		print(i, end = ' ')