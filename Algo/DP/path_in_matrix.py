def all_ways(i,j,n,m):
	if i+1==n or j+1==m:
		return 1
	if i+1>=n:
		return 0
	if j+1>=m:
		return 0
	ans = 0
	return (all_ways(i+1,j,n,m))+(all_ways(i,j+1,n,m))
def all_ways2(n,m):
	if n==1 or m==1:
		return 1
	ans = 0
	ans += all_ways2(n-1,m)+all_ways2(n,m-1)
	return ans
n,m = 3,3
res = all_ways2(n,m)
res1 = all_ways(0,0,n,m)
print(res,res1)