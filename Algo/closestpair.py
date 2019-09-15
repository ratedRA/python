import sys

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = int(input())
i = 0
j = len(b)-1
diff = sys.maxsize
while (i<len(a) and j>-1):
	if abs(a[i]+b[j]-c)<diff:
		diff = abs(a[i]+b[j]-c)
		resl = i
		resr = j
	if a[i]+b[j]>x:
		j-=1
	else:
		i+=1
print(i,j)