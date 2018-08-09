from sys import stdin,stdout
def make_set(a):
    parent[a] = a
    rank[a] = 0

def find(a):
    if a == parent[a]: return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    parentA = find(a)
    parentB = find(b)
    if parentA == parentB: return
    if rank[parentA] > rank[parentB]:
        parent[parentB] = parentA
        rank[parentA] += rank[parentB]
    else:
        parent[parentA] = parentB
        rank[parentB] += rank[parentA]

parent,rank = {},{}
n = int(stdin.readline())
for i in xrange(n):
    x,y = stdin.readline().strip().split()
    y = int(y,10)
    if x not in parent:
        make_set(x)
    if y not in parent:
        make_set(y)
    union(x,y)
for pai in parent:
    parent[pai] = find(parent[pai])
stdout.write(str(len(set(parent.values()))-1))
