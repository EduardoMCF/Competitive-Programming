from sys import stdin, stdout
r,w = stdin.readline,stdout.write

n,k = map(int,r().split())
l = r().split()
cases = [range(i,n,k) for i in xrange(k)]
eCount = sCount = Max = 0
for i in l:
    if i == '1': eCount += 1
    else: sCount += 1
for case in cases:
    e = s = 0
    for elem in case:
        if l[elem] == '1': e += 1
        else: s += 1
    Max = max(Max,abs(eCount-e - (sCount-s)))
w(str(Max))


