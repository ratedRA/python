from collections import defaultdict

a = list(map(int, input().split()))
b = list(map(int, input().split()))

d = defaultdict(lambda:int)
for i in range(len(a)):
	d[(a[i],i)] = b[i]

d = sorted(d.items(), key = lambda x:x[1])
count = 1
l = []
j = 0
for i in range(1, len(a)):
	if d[i][0][0]>=d[j][1]:
		j = i
		count+=1

return count