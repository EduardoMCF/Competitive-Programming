t,m=int(raw_input(),10),2000010
l,p=[True]*m,set([1])
for i in xrange(2,m):
    if l[i]:
        for j in xrange(i+i,m,i):l[j]=False
        p.add(i)
for i in xrange(t):
	raw_input()
	e=set(map(float,raw_input().split()))
	for i in p:
         if i not in e:
             print i-1
             break