n = raw_input()
l = map(int,raw_input().split())
c,s =0,sum(l)/2
l.sort(reverse=True)
for i in xrange(int(n)):
    c += l[i]
    if c > s: break
print i+1