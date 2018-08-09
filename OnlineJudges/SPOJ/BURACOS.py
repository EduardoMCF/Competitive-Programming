from sys import stdin,stdout
c = 1
while 1:
    setX,setY=set(),set()
    p,b = map(int,stdin.readline().split())
    if p == b == 0: break
    stdout.write('Teste ' + str(c) + '\n')
    c += 1
    if b < p:
        stdout.write('N\n')
        continue
    for i in xrange(b):
        x,y = map(int,stdin.readline().split())
        setX.add(x),setY.add(y)
    if len(setX) == len(setY) == p: stdout.write('S\n')
    else: stdout.write('N\n')
    stdout.write('\n')