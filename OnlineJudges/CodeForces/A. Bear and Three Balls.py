n = raw_input()
l = map(int,raw_input().split())
s = 'NO'
l = list(set(l))
l.sort()
for i in xrange(len(l)-2):
    if (l[i]+1 == l[i+1]) and (l[i+1]+1 == l[i+2]):
        s='YES'
        break
print s
