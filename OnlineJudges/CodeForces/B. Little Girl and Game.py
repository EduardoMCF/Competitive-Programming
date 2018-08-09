s = raw_input()
if len(s) <2:print 'First'
else:
    k,c = list(set(list(s))),0
    for i in k:
        if s.count(i)%2!=0: c+=1
    if c%2==0 and c!=0: print 'Second'
    else: print 'First'