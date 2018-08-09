n,t=map(int,raw_input().split())
k=map(int,raw_input().split())
d = 0
soma,c = 0,0
for i in xrange(n):
    soma+=k[i]
    c += 1
    if soma > t:
        v=k[d]
        soma-=v
        d+=1
        c-=1
print c