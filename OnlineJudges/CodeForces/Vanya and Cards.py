from math import ceil
n,x = map(int,raw_input().split())
s = abs(sum(map(int,raw_input().split())))
print int(ceil(s*1./x))
