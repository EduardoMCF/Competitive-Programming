from sys import stdin,stdout
from collections import deque
def make_EulerTour():
	stack,seen = deque(),[0]*n+1
	stack.appendleft(1)
	seen[1]=1
	while stack:
		node = stack.pop()
		for neighbor in graph[node]:
			if not seen[neighbor]:
				stack.appendleft(neighbor)
				seen[neighbor] = 1



r,w = stdin.readline,stdout.write
eulerTour1 = deque()
eulerTour2 = deque()

