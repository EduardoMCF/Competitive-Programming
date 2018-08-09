from collections import defaultdict
n,m = raw_input()
dictX=defaultdict(set)
k = int(raw_input(),10)
achou = False
for i in xrange(k):
    x,y = raw_input().split()
    x,y = int(x,10),int(y,10)
    dictX[x].add(y)
l = int(raw_input(),10)
for j in xrange(l):
    x,y = raw_input().split()
    x,y = int(x,10),int(y,10)
    while True:
        for w in xrange(3): ### fazer duas listas x e y e fzr bb nelas
            if dictX[x-1]:
                if y in dict[x-1]:
                    print x-1,y
                    achou = True
