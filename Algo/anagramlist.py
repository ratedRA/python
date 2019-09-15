from collections import defaultdict

s = list(input().split())
d = defaultdict(list)

def check_anagrams(s1, s2):
	count1 = [0]*256
	count2 = [0]*256
	i = 0
	while (i<len(s1) and i<len(s2)):
		count1[ord(s1[i])]+=1
		count2[ord(s2[i])]+=1
		i+=1
	if len(s1)!=len(s2):
		return False
	for i in range(256):
		if count1[i]!=count2[i]:
			return False
	return True

#s.sort()
res = defaultdict(list)
check = defaultdict(lambda:False)
for i in range(len(s)):
	sum1 = 0
	for j in s[i]:
		sum1 += ord(j)
	#print(sum1)
	flag = 0
	if (len(d[sum1])!=0):
		for el in d[sum1]:
			if check_anagrams(s[i],el[0]):
				#print('yes')
				flag = 1
				res[el[1]+1].append(i+1)
				check[i+1] = True
				check[el[1]+1] = True
				break
		if flag==0:
			d[sum1].append((s[i],i))
	else:
		d[sum1].append((s[i],i))
ans = []
fin = []
print(res)
print(check[9])

for k in range(1,len(s)+1):
	if len(res[k])==0:
		if not check[k]:
			fin.append([k])
	else:
		ans.append(k)
		ans.extend(res[k])
		ans.sort()
		fin.append(ans)
		ans = []
print(fin)
