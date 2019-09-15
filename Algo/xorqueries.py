import math

a = list(map(int, input().split()))
x = 0
xor = [0]*len(a)
xor[0] = a[0]
sum0 = [0]*len(a)
sum0[0] = a[0]
for i in range(1, len(a)):
	xor[i] = a[i]^xor[i-1]
	sum0[i] = a[i]+sum0[i-1]

q = int(input())
for i in range(q):
	l,r = map(int, input().split())
	l,r = l-1, r-1
	_xor = xor[r]^xor[l-1]
	_0sum = sum0[r] if l==0 else (sum0[r]-sum0[l-1])
	print('{0} {1}'.format(_xor, r-l+1-_0sum))

