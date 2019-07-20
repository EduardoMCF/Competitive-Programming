from sys import stdin,stdout
r,w = stdin.readline,stdout.write

n = int(r())
l = map(int,r().split())
p1,p2 = {},{}

for i in xrange(len(l)):
  if l[i] not in p1: p1[l[i]] = i
  else: p2[l[i]] = i

dist1 = p1[1]; dist2 = p2[1]
for i in xrange(2,n+1):
   dist1 += abs(p1[i] - p1[i-1])
   dist2 += abs(p2[i] - p2[i-1])
w(str(dist1 + dist2))
