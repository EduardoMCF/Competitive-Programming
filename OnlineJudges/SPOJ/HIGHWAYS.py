from collections import defaultdict
from heapq import heappush,heappop
def dijkstra(n,inicio,fim):
    vistos = [None] * (n+1)
    fila = [(0,inicio)]
    while fila:
        dist,vertice = heappop(fila)
        if vistos[vertice] is None:
            vistos[vertice] = dist
            for vizinho,distAresta in vizinhos[vertice]:
                if vistos[vizinho] is None:
                    heappush(fila,(dist + distAresta,vizinho))
        if vistos[fim] != None:
            return vistos[fim]
    return "NONE"
t = int(raw_input(),10)
for i in xrange(t):
    vizinhos = defaultdict(set)
    n,m,s,e = map(int,raw_input().split())
    for j in xrange(m):
        v1,v2,p = raw_input().split()
        v1,v2,p = int(v1,10),int(v2,10),int(p,10)
        vizinhos[v1].add((v2,p)),vizinhos[v2].add((v1,p))
    print dijkstra(n,s,e)