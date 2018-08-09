def ehPasseio(passeio):
    for i in xrange(len(passeio)-1):
        if passeio[i][1] != passeio[i+1][0]:
            return False
    return True
def intersecaoPasseios(setPasseio):
    setPasseioInverso = set()
    for aresta in passeio:
        arestaInversa = aresta[::-1]
        setPasseioInverso.add(arestaInversa)
    return setPasseio.intersection(setPasseioInverso)
n = int(raw_input(),10)
for i in xrange(n):
    vertice = raw_input()
    vizinhos = raw_input().split()
passeio = raw_input().split()
setPasseio = set(passeio)
numArestasIdeal = len(passeio)
numVerticesPasseio = len(setPasseio)
checaTrilha = False
if ehPasseio(passeio) and not intersecaoPasseios(setPasseio) and numArestasIdeal == numVerticesPasseio:
    checaTrilha = True
print checaTrilha
