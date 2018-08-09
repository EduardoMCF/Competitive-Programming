n = raw_input()
m = int(raw_input())
c,l=0,[]
for i in xrange(int(n)):
    l.append(int(raw_input()))
l.sort(reverse=True)
for i in xrange(int(n)):
    c += l[i]
    if c >= m: break
print i+1