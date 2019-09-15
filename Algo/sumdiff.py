import math

a = list(map(int, input().split()))
mod = 10**9+7
psum = [0]*len(a)
psum[0] = a[0]
res = 0

for i in range(1, len(a)):
	psum[i] += psum[i-1]+a[i]
	res+= psum[i]-a[i]

print(res)