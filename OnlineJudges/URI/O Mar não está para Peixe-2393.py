from sys import stdin,stdout
n,vistos = input(),set()
for i in xrange(n):
    x1,x2,y1,y2 = map(int,stdin.readline().split())
    [vistos.add((k,j)) for j in xrange(y1,y2) for k in xrange(x1,x2)]
stdout.write(str(len(vistos))+'\n')

