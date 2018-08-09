x = int(raw_input())
if x % 2 == 0:
    x += 1
    for i in xrange(6):
        print x
        x += 2

else:
    for i in xrange(6):
        print x
        x += 2
