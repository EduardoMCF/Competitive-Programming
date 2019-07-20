n = input()
chapters = [tuple(map(int,raw_input().split())) for _ in xrange(n)]
k = input()
for i,(l,r) in enumerate(chapters):
    if k <= r:
        print n-i
        break
else:
    print 0
