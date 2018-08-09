n = int(raw_input())
for i in range(n):
    x,y = raw_input().split()
    x,y = float(x),float(y)
    if y == 0:
        print 'divisao impossivel'
    else:
        print '%.1f' %(x/y)