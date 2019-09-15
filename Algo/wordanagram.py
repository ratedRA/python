from collections import defautldict

def comp(checks, checkp):
	for j in range(256):
			if checks[j]!=checkp[j]:
				return False
	return True

s = input()
text = input()

checks = defaultdict(lambda:0)
checkp = defaultdict(lambda:0)

for i in range(len(s)):
	checks[ord(s[i])] += 1
	checkp[ord(text[i])] += 1

for i in range(len(s), len(text)):
	if comp(checks, checkp):
		print(i-len(s))

	checkp[ord(text[i])]+=1
	checkp[ord(text[i-len(s)])]-=1

if comp(checks, checkp):
	print(len(text)-len(s))


