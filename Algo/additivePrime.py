import sys

def check_additive_prime(p,prime):
	p = str(p)
	sum1 = 0
	for i in p:
		sum1+=int(i)
	if prime[sum1]==True:
		return True
	return False
def sieve(a,n): 
	prime = [True for i in range(n+1)] 
	prime[1] = False
	p = 2
	while (p * p <= n):  
		if (prime[p] == True): 

			for i in range(p * p, n+1, p): 
				prime[i] = False
		p += 1
	flag = 0
	for p in range(a, n+1): 
		if prime[p]: 
			if check_additive_prime(p,prime):
				flag=1
				print(p, end = " ")
	if flag==0:
		print('not found')
	else:
		print()
try:
	a = sys.argv[1]
except:
	print('first number is missing')
	exit()
if a.isdigit():
	a = int(a)
else:
	print('first argument should be a number')
	exit()

try:
	b = sys.argv[2]
except:
	print('second number is missing')
	exit()
if b.isdigit():
	b = int(b)
else:
	print('second argument should be a number')
	exit()
if a>b:
	print('first number should be less than equal to second number')
else:
	sieve(a,b)