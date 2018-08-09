from collections import deque,defaultdict
from sys import stdin,stdout

def main():
    def testaPosicao(lin,col):
        if 0 <= lin <= len(matriz)-1 and 0 <= col <= len(matriz[0])-1:
            if matriz[lin][col] != "#": return True
        return False
    def bfs(pos):
        fila,achouF,achouS= deque(),False,False
        fila.append(pos)
        while fila:
            for i in xrange(len(fila)):
                vertice = fila.popleft()
                verticeL = [vertice[0],vertice[1]]
                pos1,pos2,pos3,pos4=[verticeL[0]+1,verticeL[1]],[verticeL[0]-1,verticeL[1]],[verticeL[0],verticeL[1]+1],[verticeL[0],verticeL[1]-1]
                if testaPosicao(pos1[0],pos1[1]):
                    fila.append((pos1[0],pos1[1]))
                    if matriz[pos1[0]][pos1[1]] == 'F':
                        achouF = True
                        break
                    if matriz[pos1[0]][pos1[1]] == 'S':
                        achouS = True
                if testaPosicao(pos2[0],pos2[1]):
                    fila.append((pos2[0],pos2[1]))
                    if matriz[pos2[0]][pos2[1]] == 'F':
                        achouF = True
                        break
                    if matriz[pos2[0]][pos2[1]] == 'S':
                        achouS = True
                if testaPosicao(pos3[0],pos3[1]):
                    fila.append((pos3[0],pos3[1]))
                    if matriz[pos3[0]][pos3[1]] == 'F':
                        achouF = True
                        break
                    if matriz[pos3[0]][pos3[1]] == 'S':
                        achouS = True
                if testaPosicao(pos4[0],pos4[1]):
                    fila.append((pos4[0],pos4[1]))
                    if matriz[pos4[0]][pos4[1]] == 'F':
                        achouF = True
                        break
                    if matriz[pos4[0]][pos4[1]] == 'S':
                        achouS = True
                matriz[verticeL[0]][verticeL[1]] = "#"
            if achouF:
                stdout.write("N")
                return
            else:
                if achouS:
                    stdout.write("Y")
                    return
        print stdout.write("N")
    t = int(stdin.readline(),10)
    for i in xrange(t):
        matriz = []
        n,m = stdin.readline().strip().split()
        n,m = int(n,10),int(m,10)
        for k in xrange(n):
            matriz.append([])
            c=0
            for j in stdin.readline().strip():
                if j == "E" : pos = (k,c)
                matriz[k].append(j)
                c+=1
        bfs(pos)

if __name__ == "__main__":
    main()