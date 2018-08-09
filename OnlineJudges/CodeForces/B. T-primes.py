l=[True]*1000001
l[0],l[1]=False,False
for i in xrange(2,1001):
    if l[i]:
        for j in xrange(i*i,1000001,i): l[j] = False
raw_input()
e=map(int,raw_input().split())
for i in e:
    root = int(i**0.5)
    if root == i**0.5 and l[root]:print 'YES'
    else:print 'NO'