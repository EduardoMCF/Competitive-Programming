while True:
    n = raw_input()
    if n == '0': break
    for i in xrange(int(n)):
        R = ''
        a,b,c,d,e = raw_input().split()
        if int(a) <=127: R+='A'
        if int(b) <=127: R+='B'
        if int(c) <=127: R+='C'
        if int(d) <=127: R+='D'
        if int(e) <=127: R+='E'
        if len(R)!=1: R='*'
        print R
