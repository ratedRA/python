a = list(map(int, input().split()))
ma = 0
for i, x in enumerate(a):
	ma = max(ma, x)
	if i==ma:
		ans+=1
return ans