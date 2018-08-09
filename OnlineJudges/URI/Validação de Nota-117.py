l =[]
while True:
    n = float(raw_input())
    if n < 0 or n > 10:
        print 'nota invalida'
    else:
        l.append(n)
    if len(l)==2:
        print 'media = %.2f' %(sum(l)/2)
        break
