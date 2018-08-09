while True:
    r = ''
    b, n = raw_input().split()
    if b + n == '00': break
    R = raw_input().split()
    for i in xrange(int(n)):
        d, c, v = raw_input().split()
        R[int(d) - 1] = int(R[int(d) - 1]) - int(v)
        R[int(c) - 1] = int(R[int(c) - 1]) + int(v)
    for i in R:
        if i < 0:
            r = 'N'
            break
        r = 'S'
    print r





