from sys import stdin,stdout
def make_set(a):
    parent[a] = a
    rank[a] = 1

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    parentA = find(a)
    parentB = find(b)
    if parentA == parentB: return
    if rank[parentA] < rank[parentB]:
        parent[parentA] = parentB
        rank[parentB] += rank[parentA]
    else:
        parent[parentB] = parentA
        rank[parentA] += rank[parentB]

parent,rank = {},{}
n,m = map(int,stdin.readline().split())

for i in xrange(m):
    x,y = map(int,stdin.readline().split())
    if x not in parent: make_set(x)
    if y not in parent: make_set(y)
    union(x,y)
for filho in parent:
    parent[filho] = find(parent[filho])
stdout.write(str(2**(len(parent)-len(set(parent.values())))))

