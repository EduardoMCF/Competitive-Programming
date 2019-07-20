from math import ceil
n, k = map(int,raw_input().split())
print sum(map(lambda x: int(ceil(x)),[n*2./k,n*5./k,n*8./k]))
