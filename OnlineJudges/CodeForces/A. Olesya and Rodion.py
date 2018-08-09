n,t=raw_input().split()
if int(t)!=10:print t*int(n)
else:
    if int(n)>1: print 10**(int(n)-1)
    else: print -1