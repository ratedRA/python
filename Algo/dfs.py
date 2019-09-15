import math
from collections import defaultdict


# FOR GRAPH WE NEED NOT TO CONSIDER SEPERATLEY FOR EACH NODE AS TREES ARE CONNECTED. Directly start 
# from the root.

def dfs(node, visited, graph):
	print(node)
	visited[node] = True

	for neig in graph[node]:
		if not visited[neig]:
			dfs(neig, visited, graph)

def all_node_dfs(visited, graph):

	for i in range(1, n+1):
		print('for node %d'%(i))
		visited = [False]*(n+1)
		dfs(i, visited, graph)

n, m = map(int, input('enter the number of nodes and edges').split())
graph = defaultdict(list)
for i in range(m):
	x,y = map(int, input().split())
	graph[x].append(y)
	graph[y].append(x)

visited = [False]*(n+1)
all_node_dfs(visited, graph)

