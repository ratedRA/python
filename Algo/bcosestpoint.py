import math

def distance(a,b):
	return math.sqrt((a**2)+b**2)

n = int(input())
m = []
b = int(input())
for i in range(n):
	a = []
	x,y = map(int, input().split())
	m.append([x,y])

res = []
for i in m:
	a, b = i[0], i[1]
	edistance = distance(a,b)
	res.append(edistance)
res.sort()
print(res[:b])

