n = int(raw_input())
a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
g = b-c
t=0
if g < a and b <= n:
    t+=(n-b)/(b-c) + 1
    n -= t*g
if a <= n:
    t+=n/a
print t

