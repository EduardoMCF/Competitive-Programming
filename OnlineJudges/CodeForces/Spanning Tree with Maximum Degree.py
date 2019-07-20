from sys import stdin,stdout
from collections import defaultdict as dd
r,w = stdin.readline,stdout.write
parent = {};rank = {};graph = {}

def make_set(vertice):
    parent[vertice] = vertice;rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)
    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return minimum_spanning_tree

n,m = map(int,r().split())
degree = dd(int);edges = [];graph['vertices'] = map(str,xrange(1,n+1))
for i in xrange(m):
    x,y = r().split()
    degree[x] += 1; degree[y] += 1; edges.append([777,x,y])
targetNode = max(degree.iterkeys(), key = (lambda k: degree[k])); maxDegree = degree[targetNode]
c=0
for edge in edges:
    if targetNode in edge: edge[0] = 0; c+=1
    if c >= maxDegree: break
graph['edges'] = set(map(tuple,edges))
print '\n'.join([' '.join(edge[1:]) for edge in kruskal(graph)])
