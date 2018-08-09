from sys import stdin,stdout
def make_set(a):
    parent[a] = a

def union(a,b):
    parent[b] = a

parent,setX,setY = {},set(),set()
n = int(stdin.readline(),10)
res = [[] for j in xrange(n)]
for i in xrange(n):
    x,y = map(int,stdin.readline().split())
    if x not in setX and x not in setY: make_set(x)
    if y not in setY and y not in setY: make_set(y)
    setX.add(x),setY.add(y)
    union(x,y)
if n == 2: stdout.write(str(parent[0]) + ' ' + str(list(setY.difference(setX))[0]))
elif n == 3: stdout.write(str(list(setX.difference(setY))[0]) + ' ' + str(parent[0]) + ' ' + str(list(setY.difference(setX))[0]))
else:
    ultimo,penultimo = list(setY.difference(setX))[0],parent[0]
    res[-1],res[-2],c = str(ultimo),str(penultimo),2
    par = True if n%2 else False
    while 1:
        ultimo,penultimo = parent[ultimo],parent[penultimo]
        res[-1-c],res[-2-c] = str(ultimo),str(penultimo)
        if par:
            if parent[penultimo] == penultimo or parent[penultimo] == 0: break
        else:
            if parent[ultimo] == ultimo or parent[ultimo] == 0: break
        c += 2
    if par:res[0] = str(parent[ultimo])
    stdout.write(' '.join(res))
