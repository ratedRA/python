import math
from collections import defaultdict

def bfs(source, graph, n):
	q = []
	visited = [False]*(n+1)
	visited[source] = True
	q.append(source)
	while q:
		vertex = q.pop(0)

		print(vertex, end = " ")
		for neighbours in graph[vertex]:
			if visited[neighbours] == False:
				q.append(neighbours)
				visited[neighbours] = True

n, m = map(int,input('enter the number of vertices and edges: ').split())
graph = defaultdict(list)
print("enter the edges: ")
for i in range(m):
	x, y = map(int, input().split())
	graph[x].append(y)
	graph[y].append(x)

s = int(input('enter the source vertex: '))
bfs(s, graph, n)
