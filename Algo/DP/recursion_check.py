def sum_of_array(a,n):
	if n==0:
		return 0
	sum1 = 0
	count1 = 0
	sum1 += a[n-1]+sum_of_array(a,n-1)
	count1+=1
	print(count1)
	return sum1

a = list(map(int, input().split()))
res = sum_of_array(a, len(a))
print(res)