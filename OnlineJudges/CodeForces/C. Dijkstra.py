from collections import defaultdict
from heapq import heappush,heappop
def dijkstra(n,inicio,fim):
    vistos = [None] * (n+1)
    fila = [(0,inicio)]
    parent = [0] * (n+1)
    while fila:
        dist,vertice = heappop(fila)
        if vistos[vertice] is None:
            vistos[vertice] = dist
            for vizinho,distAresta in vizinhos[vertice]:
                if vistos[vizinho] is None:
                    parent[vizinho] = vertice
                    heappush(fila,(dist + distAresta,vizinho))
        if vistos[fim] != None:
            daddy = n
            print vistos[fim],parent[5],parent[parent[5]],parent[parent[parent[5]]],parent[parent[parent[parent[5]]]]
            while daddy != 0:
                print daddy,
                daddy = parent[daddy]
            return
    else: print -1
vizinhos = defaultdict(set)
n,m = map(int,raw_input().split())
for j in xrange(m):
    v1,v2,p = raw_input().split()
    v1,v2,p = int(v1,10),int(v2,10),int(p,10)
    vizinhos[v1].add((v2,p)),vizinhos[v2].add((v1,p))
dijkstra(n,1,n)