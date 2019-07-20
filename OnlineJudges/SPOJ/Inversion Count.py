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

it = int
t = it(r(),10)

buffer = ''
for i in xrange(t):
    bl = r()
    n = it(r(),10)
    arr = [(it(r(),10),j) for j in xrange(n)]
    sortd = sorted(arr)

    newArr,c = [0]*n,0
    newArr[sortd[0][1]] = 0
    bit = [0]*(n+1)

    for j in xrange(1,n):
        if sortd[j][0] != sortd[j-1][0]:
            c += 1
        newArr[sortd[j][1]] = c

    inv = 0
    for elem in reversed(newArr):
        inv += read(elem)
        update(elem,1,n)

    buffer += str(inv)+'\n'

w(buffer)
