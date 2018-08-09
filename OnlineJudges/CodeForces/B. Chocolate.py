raw_input()
b = raw_input().strip('0 ').split()
pos,m=[],1
for i in xrange(len(b)):
    if b[i] == '1':pos.append(i)
if not pos: print 0
else:
    for i in xrange(len(pos)-1):
        s = pos[i+1]-pos[i]
        m *= s
    print m