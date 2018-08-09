def main():
	from sys import stdin,stdout
	from collections import deque
	r,w,m = stdin.readline,stdout.write,map

	def BFS(dist):
		while queue:
			node = queue.popleft()
			for neighbor in graph[node]:
				if not seen[neighbor]: 
					queue.append(neighbor);	seen[neighbor],dist[neighbor] = 1,dist[node]+1

	n,x = m(int,r().split())
	graph = [[] for i in xrange(n+1)]

	for i in xrange(n-1):
		a,b = map(int,r().split())
		graph[a].append(b), graph[b].append(a)

	queue,seen,cont,distToRoot = deque(),[0]*(n+1),1,[0]*(n+1)
	queue.append(1);seen[1] = 1
	BFS(distToRoot)

	queue,seen,cont,distToX = deque(),[0]*(n+1),1,[0]*(n+1)
	queue.append(x);seen[x] = 1
	BFS(distToX)

	maxDist = 0
	for i in xrange(1,n+1):
		if distToRoot[i] > distToX[i]: maxDist = max(maxDist,distToRoot[i])

	w(str(2*maxDist))
main()