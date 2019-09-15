from collections import defaultdict

a = list(map(int, input().split()))
b = list(map(int, input().split()))

d = defaultdict(lambda:int)
for i in range(len(a)):
	d[(a[i],i)] = b[i]

d = sorted(d.items(), key = lambda x:x[1], reverse = True)
count = 0
days = defaultdict(lambda:-1)
for i in range(len(d)):
	x = d[i][0][0]
	if days[x]==-1:
		days[x] = 1
		count+=d[i][1]
	else:
		x-=1
		while x>0:
			if days[x]==-1:
				days[x] = 1
				count+=d[i][1]
				break
			else:
				x-=1
print(count)
			


