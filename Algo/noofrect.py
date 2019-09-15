a = list(map(int, input().split()))
b = int(input())
i = 0
n = len(a)
j = n-1
res = 0
while i<j:
	pro = a[i]*a[j]
	if pro<b:
		x = j-i
		res+=x*2
		i+=1
	else:
		j-=1
for i in range(len(a)):
	if a[i]*a[i]<b:
		res+=1
print(res)