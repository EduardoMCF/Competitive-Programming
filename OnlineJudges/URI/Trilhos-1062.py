from collections import deque
while True:
    n = int(raw_input())
    if n == 0: break
    while True:
        l, p,a = [], deque(),n
        l = map(int,raw_input().split())
        if l == [0]:break
        for i in reversed(l):
            if i == a:
                a-=1
                while True:
                    if p and p[0] == a:
                        p.popleft()
                        a-=1
                    else: break
            else:p.appendleft(i)
        print 'Yes' if not p else 'No'
    print ""

