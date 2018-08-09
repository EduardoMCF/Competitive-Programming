from collections import defaultdict
hall,vits = defaultdict(int),set()
while True:
    try:
        a,v = raw_input().split()
        if a != v:
            hall[a]+=1
            vits.add(v)
    except EOFError:break
print 'HALL OF MURDERERS'
for i in sorted(hall.keys()):
    if i not in vits: print i,hall[i]