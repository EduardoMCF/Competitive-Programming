n,m = map(int,raw_input().split())
palavra = raw_input()
for i in xrange(m):
    x,y,c1,c2 =raw_input().split()
    x,y = int(x,10),int(y,10)
    palavra = palavra[:x-1] + palavra[x-1:y].replace(c1,c2) + palavra[y:]
print palavra