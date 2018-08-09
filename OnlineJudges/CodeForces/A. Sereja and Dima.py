t,s,d = 1,0,0
n = raw_input()
k = map(int,raw_input().split())
while True:
    if len(k) == 0: break
    if k[0] > k[-1]:
        m= k[0]
        del(k[0])
    else:
        m = k[-1]
        del(k[-1])
    if t == 1: s += m
    else: d += m
    t *= -1
print s,d