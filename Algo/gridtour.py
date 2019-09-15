import math
from collections import defaultdict

def bfs(source, graph, n):
	q = []
	visited = [False]*(n+1)
	visited[source] = True
	q.append(source)
	count = 0
	while q:
		vertex = q.pop(0)
		count+=1
		#print(vertex, end = " ")
		for neighbours in graph[vertex]:
			print('neugh',neighbours)
			if visited[neighbours] == False:
				q.append(neighbours)
				visited[neighbours] = True

	return count

t = int(input())
while t>0:
	n, m, k = map(int, input().split())
	graph = defaultdict(list)
	for i in range(n):
		for j in range(m):
			x = (i+n)%k
			y = (j+m)%k
			c = m*i+j
			z= x*m+y
			x = x*m+j
			y = m*i+y

			graph[c].append(x)
			graph[c].append(y)
			graph[c].append(z)
	min1 = math.inf
	for i in range(n):
		for j in range(m):
			res = bfs((i*m+j), graph, n*m)
			if res==1:
				print(-1)
			else:
				print(res)
	t-=1
