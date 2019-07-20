from sys import stdin,stdout
read,write = stdin.readline,stdout.write

n,maxh,k = map(int,read().split())
potatoes = map(int,read().split())

pp = h = s = 0
while 1:
    if pp >= n:
        s += h/k if h>k or not h else 1
        break
    while h < maxh and pp < n:
        if maxh-h < potatoes[pp]: break
        h += potatoes[pp]
        pp += 1
    s += h/k if h>k else 1
    h = h%k if h>k else 0
print s
