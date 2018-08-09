n,t = raw_input().split()
n,t = int(n,10),int(t,10)
fila = list(raw_input())
s = ''
for i in xrange(t):
    c = 0
    for j in xrange(n-1):
        if j + c >= n - 1: break
        if fila[j+c] == 'B' and fila[j+c+1] == 'G':
            fila[j+c],fila[j+c+1] = 'G','B'
            c += 1
print "".join(fila)