from sys import stdin,stdout
def main():
    def make_set(vertice):
        parent[vertice] = vertice

    def find(vertice):
        if vertice == parent[vertice]:
            return vertice
        parent[vertice] = find(parent[vertice])
        return parent[vertice]

    def union(a,b):
        parentA = find(a)
        parentB = find(b)
        if parentA != parentB:
            parent[parentB] = parentA

    def kruskal():
        soma = 0
        for peso,vertice1,vertice2 in arestas:
            if find(vertice1) != find(vertice2):
                union(vertice1,vertice2)
                soma += peso
        return soma

    arestas,parent = [],{}
    n,m = map(int,stdin.readline().split())
    for i in xrange(m):
        v1,v2,p = map(int,stdin.readline().split())
        make_set(v1),make_set(v2)
        arestas.append((p,v1,v2))
        # Tentei usar heapq aqui: heappush(heap,(p,v1,v2))
        # Problema: A ordenacao nao sai como deveria.
        # Ex:
        # Passo 1: heappush(heap,(1,1,2)) ======> heap = [(1,1,2)]
        # Passo 2: heappush(heap,(20,1,2)) ======> heap = [(1,1,2),(20,1,2)]
        # Passo 3: heappush(heap,(2,2,2)) ======> heap = [(1,1,2),(20,1,2),(1,2,2)] ERRO!
    arestas.sort()
    stdout.write(str(kruskal()))

if __name__ == "__main__":
    main()
