import math
from collections import defaultdict

def bfs(source, graph, n, w, k):
	q = []
	visited = [False]*(n+1)
	visited[source] = True
	q.append(source)
	count = 0
	while q:
		vertex = q.pop(0)
		sum1 = 0
		for neighbours in graph[vertex]:
			if visited[neighbours] == False:
				q.append(neighbours)
				sum1+=w[neighbours-1]
				if sum1>k:
					graph[vertex].remove(neighbours)
					graph[neighbours].remove(vertex)
					sum1-=w[neighbours-1]
					count+=1
				visited[neighbours] = True
	return count

n, k = map(int,input().split())
w = list(map(int, input().split()))
graph = defaultdict(list)
for i in range(n-1):
	x, y = map(int, input().split())
	graph[x].append(y)
	graph[y].append(x)

s = 1
print(bfs(s, graph, n, w, k))
