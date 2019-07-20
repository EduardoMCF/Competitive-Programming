from sys import stdin,stdout
r,w = stdin.readline,stdout.write

n = int(r(),10)
l = map(int,r().split())
l.sort()

max = j = 0
for i in range(n):
  while(j < n and abs(l[j]-l[i]) <= 5): j += 1
  if max < j-i:
      max = j-i
w(str(max))
