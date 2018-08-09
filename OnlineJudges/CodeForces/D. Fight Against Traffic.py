from sys import stdin,stdout
from collections import defaultdict,deque

def BFS(level,node):
	queue,seen,cont = deque(),set(),1
	queue.append(node)
	while queue:
		Node = queue.popleft()
		for neighbor in graph[Node]:
			if not level[neighbor]:
				queue.append(neighbor)
				level[neighbor] = level[Node]+1
	level[node]=0

r,w = stdin.readline,stdout.write
n,m,s,t = map(int,r().split())
graph,levelS,levelT = defaultdict(list),defaultdict(int),defaultdict(int)
f_graph = [[0]*n for i in xrange(n)]

for i in xrange(m):
	x,y = map(int,r().split())
	graph[x].append(y),graph[y].append(x)
	f_graph[min(x,y)-1][max(x,y)-1] = 1

BFS(levelS,s)
BFS(levelT,t)
dist = levelS[t]
ans = 0

for i in xrange(1,n+1):
	for j in xrange(i+1,n+1):
		if (not f_graph[i-1][j-1]) and (levelT[i] + levelS[j] + 1 >= dist) and (levelS[i] + levelT[j] + 1 >= dist):	ans += 1
w(str(ans))
