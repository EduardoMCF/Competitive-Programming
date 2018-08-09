n,m = map(int,raw_input().split())
tabuleiro = []
for i in xrange(n):
    c,f,check = 0,'',False
    l = raw_input()
    if i%2 == 0:
        for j in l:
            if j == '-':
                f = f + '-'
                if check: c+=1
            else:
                if c%2==0:f = f + 'B'
                else: f = f + 'W'
                c+=1
                check = True
    else:
        for j in l:
            if j == "-":
                f = f + '-'
                if check: c += 1
            else:
                if c%2==0: f = f + 'W'
                else: f = f + 'B'
                c+=1
                check = True
    print f



