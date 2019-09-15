a = list(map(int, input().split()))

b = int(input())
bad = 0
count = 0
for i in range(len(a)):
	if a[i]<=b:
		count+=1
for i in range(count):
	if a[i]>b:
		bad+=1
i = 0
j = count
ans = bad
while j<len(a):
	if a[i]>b:
		bad-=1
	if a[j]>b:
		bad+=1
	i+=1
	j+=1
	ans = min(ans,bad)
return ans

