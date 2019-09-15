import math

def total_money(n, m):
	a = [0]*n
	for i in range(len(m)):
		x, b, c = m[i]
		for j in range(x-1,b):
			a[j]+=c
	return a

n = int(input())
m = []
while True:
	a = list(map(int, input().split()))
	m.append(a)
	if input('press y if want to stop') == 'y':
		break
res = total_money(n, m)
print(res)