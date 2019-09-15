import math

a = list(map(int, input().split()))
xor = 0
for i in a:
	xor^=a[i]
print(xor)