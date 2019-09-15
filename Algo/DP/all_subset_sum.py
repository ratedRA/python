def all_sum(a,i,subset,res):
	if i==len(a):
		print(subset)
		res.append(sum(subset))
		return
	if i<len(a):
		subset.append(a[i])
		all_sum(a,i+1,subset,res)
	if len(subset)>0:
		subset.pop()
		all_sum(a,i+1,subset,res)
a = list(map(int, input().split()))
res = []
all_sum(a,0,[],res)
print(res)