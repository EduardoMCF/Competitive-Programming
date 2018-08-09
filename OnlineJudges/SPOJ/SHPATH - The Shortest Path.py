from collections import defaultdict
from heapq import heappush,heappop
from sys import stdin,stdout

def main():
    cidades, vizinhos= {}, defaultdict(set)
    t = int(stdin.readline(),10)
    for i in xrange(t):
        nv = int(stdin.readline(),10)

        for j in xrange(nv):
            cidades[stdin.readline().strip()] = j+1
            nvz = int(stdin.readline(),10)

            for k in xrange(nvz):
                v2,peso = stdin.readline().strip().split()
                v2,peso = int(v2,10),int(peso,10)
                vizinhos[j + 1].add((v2, peso))

        r=int(stdin.readline(),10)

        for h in xrange(r):
            ini,fim = stdin.readline().strip().split()
            inicio, fim = cidades[ini],cidades[fim]

            # Funcao dijkstra
            vistos = [None] * (nv + 1)
            fila = [(0, inicio)]
            while fila:
                dist, vertice = heappop(fila)
                if vistos[vertice] is None:
                    vistos[vertice] = dist
                    if vistos[fim] != None:
                        stdout.write(str(vistos[fim]) + '\n')
                        break
                    for vizinho, distAresta in vizinhos[vertice]:
                        if vistos[vizinho] is None:
                            heappush(fila, (dist + distAresta, vizinho))

        if i != t-1: raw_input()

if __name__ == "__main__":
    main()