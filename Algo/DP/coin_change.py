def coin_change(a,k,i):
	if k==0:
		return 1
	if k<0:
		return 0
	ans = 0
	while (i<len(a) and k-a[i]>=0):
		ans+=coin_change(a,k-a[i],i)
		#print(ans)
		#return ans
		i+=1
	return ans

a = list(map(int, input().split()))
print(coin_change(a,4,0))
