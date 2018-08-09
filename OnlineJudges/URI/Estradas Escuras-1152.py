def make_set(vertice):
    parent[vertice]=vertice
def find(vertice):
    if vertice == parent[vertice]: return vertice
    parent[vertice] = find(parent[vertice])
    return parent[vertice]
def union(a,b):
    parentA = find(a)
    parentB = find(b)
    if parentA != parentB:
        parent[parentB] = parentA
def kruskal():
    soma = 0
    for peso,vertice1,vertice2 in sorted(arestas):
        if find(vertice1) != find(vertice2):
            union(vertice1,vertice2)
            soma += peso
    return soma
while True:
    parent,arestas=dict(),set()
    n,m = map(int,raw_input().split())
    if n+m == 0: break
    somatotal = 0
    for i in xrange(m):
        v1,v2,p = raw_input().split()
        v1,v2,p = int(v1,10),int(v2,10),int(p,10)
        make_set(v1),make_set(v2)
        somatotal += p
        edge = (p,v1,v2)
        arestas.add(edge)
    print somatotal - kruskal()