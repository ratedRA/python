import bisect

a = list(map(int, input().split()))
newlist = []
res = []
for i in a[::-1]:
	pos = bisect.bisect_left(newlist, i)
	newlist.insert(pos, i)
	res.append(pos)
print(res[::-1])