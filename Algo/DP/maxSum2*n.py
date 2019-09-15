m = []
n = int(input())
for i in range(n):
	a = list(map(int, input().split()))
	m.append(a)

arrinc = [0]*(n)
arrexc = [0]*(n)

arrinc[0] = max(m[0][0],m[0][1])

for i in range(1, n):
	curr_max = max(m[i][0], m[i][1])
	arrinc[i] = curr_max+arrexc[i-1]
	arrexc[i] = max(arrinc[i-1],arrexc[i-1])
print(max(arrinc[n-1], arrexc[n-1]))