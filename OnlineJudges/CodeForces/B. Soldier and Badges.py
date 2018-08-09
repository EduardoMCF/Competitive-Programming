n = raw_input()
l = map(int, raw_input().split())
l.sort()
c=0
for i in xrange(int(n)):
     s = l.count(l[i])
     if s > 1:
         for j in xrange(1,s):
             l[i+j] += 1
             c+=1
print c
