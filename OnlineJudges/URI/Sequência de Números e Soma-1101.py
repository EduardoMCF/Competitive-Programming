while True:
    m,n = raw_input().split()
    m,n = int(m), int(n)
    if m <= 0 or n <= 0:
        break
    if m > n:
        maior = m
        menor = n
    else:
        maior = n
        menor = m
    for i in range(menor,maior+1):
        print i,
    print 'Sum=%i' %sum(range(menor,maior+1))