def main():
	from sys import stdin,stdout
	from collections import deque
	r,w = stdin.readline, stdout.write
	
	n = int(r(),10)
	graph = [[] for i in xrange(n+1)]
	
	for i in xrange(n-1):
		x,y = map(int,r().split())
		graph[x].append(y),graph[y].append(x)
	
	maxx = 0; maxpos = 0;
	for i in xrange(len(graph)):
		if len(graph[i])>maxx:	maxx = len(graph[i]); maxpos = i
	
	colors = xrange(1,maxx+2)
	queue,color = deque([(1,0)]),[0]*(n+1)
	color[1] = 1;color[0] = -1
	c = 1
	while queue:
		node,parent = queue.popleft()
		for neighbor in graph[node]:
			if not color[neighbor]:	
				while colors[c%len(colors)] == color[node] or colors[c%len(colors)] == color[parent]:
					c += 1
				color[neighbor] = colors[c%len(colors)];queue.append((neighbor,node));c += 1

	w(str(maxx+1)+'\n')
	for i in xrange(1,n+1):w("%i " %(color[i]))
				
main()