import heapq

a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
k = int(input())

n = len(a)

i = n-1
j = n-1

sum1 = a[i]+b[j]
q = []
heapq.heappush(q, (-1*sum1, (i,j)))
check = set()
check.add((i,j))
res = []
count = 0
while count<k:
	x = heapq.heappop(q)
	val = x[0]*-1
	res.append(val)
	count+=1
	if count == k:
		break
	i = x[1][0]
	j = x[1][1]
	if i-1>-1:
		sum1 = a[i-1]+b[j]
	if j-1>-1:
		sum2 = a[i]+b[j-1]

	if ((i-1,j)) not in check:
		heapq.heappush(q, (-sum1, (i-1,j)))
		check.add((i-1,j))
	if ((i,j-1)) not in check:
		heapq.heappush(q, (-sum2, (i,j-1)))
		check.add((i,j-1))
print(res)


