import math
from collections import defaultdict
import heapq

def find_path_frm_source(predecessor, vertex):
	while predecessor[vertex]!=None:
		print(predecessor[vertex], end = " ")
		vertex = predecessor[vertex]

def dijkstra(n, source, graph, predecessor, mindistance):
	mindistance[source] = 0
	q = [] # for the priority queue
	heapq.heappush(q,(0, source))
	visited = [False]*n

	while q:
		path_len, vertex = heapq.heappop(q)
		if visited[vertex]:
			continue
		else:
			visited[vertex] = True
			for y, w in graph[vertex].items():
				newd = mindistance[vertex] + w
				if newd < mindistance[y]:
					mindistance[y] = newd
					predecessor[y] = vertex
					heapq.heappush(q,(newd, y))

	return mindistance, predecessor

n, m = map(int,input('enter the number of vertices and edge: ').split())

graph = defaultdict(defaultdict)

print('enter the edges and their corresponding weights')
for i in range(m):
	x,y,w = map(int,input().split())
	graph[x][y] = w
	graph[y][x] = w

predecessor = [None]*n
mindistance = [math.inf]*n
s = int(input('enter the source vertex:'))
mindis, pred = dijkstra(n, s, graph, predecessor, mindistance)
print(mindis, pred)
x = int(input('input the node you want to know the mindistance paths of: '))
find_path_frm_source(pred, x)

'''
8 16

0 1 5
0 2 8
0 3 9
1 4 12
1 6 15
2 4 7
2 5 6
3 5 4
3 7 20
4 6 3
4 5 1
4 7 11
5 7 13
6 7 9
1 2 4
3 2 5

source - 0

sol - [0, 5, 8, 9, 14, 13, 17, 25] [None, 0, 0, 0, 5, 3, 4, 4]
'''