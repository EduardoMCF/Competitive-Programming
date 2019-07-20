from sys import stdin,stdout
read,write = stdin.readline,stdout.write

n = int(read())
pos = {}
for i,v in enumerate(map(int,read().split())):
    pos[v] = i

res1 = res2 = 0
int(read())
for i in map(int,read().split()):
    res1 += pos[i] + 1
    res2 += n - pos[i]
print res1,res2
