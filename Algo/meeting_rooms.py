import sys
n = int(input())
m = []
for i in range(n):
	a,b = input().split()
	m.append([a,b])
s = []
e = []
for i in m:
	s.append(i[0])
	e.append(i[1])
s.sort()
e.sort()

i = 0
j = 0
new= []
while (i<len(s) and j<len(e)):
	if (s[i]<e[j]):
		i+=1
		new.append(str(s[i])+'s')
	elif s[i]>e[j]:
		j+=1
		new.append(str(e[j])+'e')
	else:
		new.append(str(e[j])+'e')
		j+=1
while (i<len(s)):
	new.append(str(s[i])+'s')
	i+=1
while (j<len(e)):
	new.append(str(e[j])+'e')
	j+=1



max1 = -(sys.maxsize)
count = 0

for i in new:
	if i[-1] == 's':
		count+=1
		if count>max1:
			max1 = count
	else:
		count-=1

print(max1)

