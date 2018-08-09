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
    mc = []
    for peso,vertice1,vertice2 in arestas:
        if find(vertice1) != find(vertice2):
            union(vertice1,vertice2)
            mc.ap((vertice1,vertice2,peso))
    return mc
cont = 1
while True:
    arestas,parent=[],{}
    n,m = map(int,raw_input().split())
    if not n+m: break
    for i in xrange(m):
        v1,v2,p = raw_input().split()
        v1,v2,p = int(v1,10),int(v2,10),int(p,10)
        make_set(v1),make_set(v2)
        arestas.append((p,v1,v2))
    arestas.sort()
    if cont > 1: print
    print "Teste",cont
    for j in kruskal():
        res[j]
    cont += 1
