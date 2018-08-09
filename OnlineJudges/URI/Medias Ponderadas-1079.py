n = int(raw_input())
for i in range(n):
    a,b,c = raw_input().split()
    a,b,c=float(a),float(b),float(c)
    media = (a*2+b*3+c*5)/10
    print '%.1f' %media