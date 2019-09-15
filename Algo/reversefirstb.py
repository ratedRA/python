from collections import deque

a = list(map(int, input().split))
b = int(input())

q = deque()
s = []

for i in a:
	q.append(i)

for i in range(b):
	s.append(q.popleft())
while len(s)>0:
	q.append(s[-1])

while len(q)-b>0:
	q.append(q.popleft())

return q
