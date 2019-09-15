import math

a = list(map(int, input().split()))
x = int(input())
pa = [0]*len(a)
pa[0] = a[0]
for i in range(1, len(a)):
	pa[i]+=a[i]+pa[i-1]

l = 0
n = len(a)
h = n
ans = -1

while l<=h:
	mid = (l+h)//2
	print('mid',mid)
	flag = 1
	res = 0

	for i in range(mid, n):
		res=1
		#print(pa[i],pa[i-mid])
		if pa[i]-pa[i-mid]>x:
			flag = 0
			break

	if flag==res==1:
		ans = mid
		l = mid+1
	else:
		h=mid-1
if pa[n-1]<=x:
	ans+=1
print(ans)