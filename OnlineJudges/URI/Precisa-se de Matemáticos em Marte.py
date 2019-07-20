from sys import stdin,stdout
r,w = stdin.readline,stdout.write

def build(n):
    for i in xrange(n):
        update(i,arr[i],n)

def read(idx):
    acc = 0
    idx += 1
    while idx:
        acc += bit[idx]
        idx -= idx & -idx
    return acc

def update(idx,val,n):
    idx += 1
    while idx <= n:
        bit[idx] += val
        idx += idx & -idx

it,st = int,str
n = it(r(),10)
arr = map(it,r().split())

bit = [0]*(n+1)
build(n)

buffer = ''
while True:
    inp = r().split()
    if not inp: break
    t,v = inp
    v = it(v,10)-1
    if t == 'a':
        update(v,-arr[v],n)
    else:
        buffer += str(read(v-1))+'\n'

w(buffer)
