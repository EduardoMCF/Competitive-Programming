from sys import stdin,stdout
from collections import defaultdict
from heapq import heappush,heappop
def dijkstra(n,inicio,fim):
    vistos = [None] * (n+1)
    fila = [(0,inicio)]
    rank = 0
    while fila:
        dist,vertice = heappop(fila)
        if vistos[vertice] is None:
            vistos[vertice] = dist
            if vistos[fim] != None:
                return str(vistos[fim])
            for vizinho,distAresta in vizinhos[vertice]:
                if vistos[vizinho] is None:
                    heappush(fila,(dist + distAresta,vizinho))
    return "Nao e possivel entregar a carta"


while 1:
    vizinhos = defaultdict(set)
    n,e = map(int, stdin.readline().strip().split())
    if not n+e: break
    for k in xrange(e):
        v1,v2,p = map(int,stdin.readline().strip().split())
        vizinhos[v1].add((v2,p))
    c = int(stdin.readline(),10)
    for j in xrange(c):
        ver1,ver2 = map(int,stdin.readline().strip().split())
        if ver2 in vizinhos[ver1][0]: stdout.write('0')
        else:stdout.write(dijkstra(n,ver1,ver2))


