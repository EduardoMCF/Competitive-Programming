from sys import stdin,stdout
k,l,m = map(int,stdin.readline().split())
p = map(int,stdin.readline().split())
M = max(p)+1
estados = [[]]*(M)
estados[0] = 0
estados[k]=estados[l]=estados[1]=1
for i in xrange(2,M):
    if not estados[i]:
        if not estados[i-1] or (not estados[i-k] and i>k) or (not estados[i-l] and i>l):estados[i]=1
        else:estados[i]=0
for j in p:
    if estados[j]: stdout.write('A')
    else: stdout.write('B')
