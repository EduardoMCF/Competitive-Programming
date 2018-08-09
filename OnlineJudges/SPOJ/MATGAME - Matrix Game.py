from sys import stdin,stdout
n = input()
for i in xrange(n):
    n,m = map(int,stdin.readline().split())
    somas,pesos = [],[]
    for j in xrange(n):
        p= map(int,stdin.readline().split())
        x = p[0]
        s = sum(p)
        somas.append(s)
        pesos.append(x)
    if n == 1:
        a, q = pesos[0], somas[0]
        if a == 1:stdout.write('FIRST\n') if q%2 else stdout.write('SECOND\n')
        else:
            estados =[[]] * (somas[0]+1)
            estados[0]=0

            for i in xrange(1,a+1): estados[i]=1
            for l in xrange(a+1,q+1):
                for u in xrange(1,a+1):
                    if not estados[l-u]:
                        estados[l] = 1
                        break
                else: estados[l]=0
            stdout.write('FIRST\n') if estados[q] else stdout.write('SECOND\n')
    else:
        xor=somas[0]
        for k in xrange(1,len(somas)):xor^=somas[k]
        stdout.write('FIRST\n') if xor else stdout.write('SECOND\n')
    stdin.readline()

