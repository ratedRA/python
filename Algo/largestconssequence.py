from collections import defaultdict

a = list(map(int, input().split()))
d = defaultdict(lambda:0)

for i in range(len(a)):
	d[a[i]]+=1
ans = 0
for i in range(len(a)):
	if a[i]-1 not in d:
		j = a[i]
		while d[j]!=0:
			j+=1

		ans = max(ans, j-a[i])
print(ans)