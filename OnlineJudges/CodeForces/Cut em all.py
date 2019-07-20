def main():
    from sys import stdin,stdout
    read,write = stdin.readline,stdout.write
    n = int(read())

    def DFS_Iterative(v):
        from collections import deque
        stack = deque([v])
        parent = [0]*(n+1)
        count = [1]*(n+1)
        while stack:
            v = stack[0]
            flag = True

            if not parent[v]:
                parent[v] = 1

            for neighbor in graph[v]:
                if not parent[neighbor]:
                    stack.appendleft(neighbor)
                    parent[neighbor] = v
                    flag = False

            if flag:
                stack.popleft()
                count[parent[v]] += count[v]

        return sum(1 for num in count[2:] if not num&1)

    graph = [[] for _ in xrange(n+1)]
    for i in xrange(n-1):
        x,y = map(int,read().split())
        graph[x].append(y), graph[y].append(x)

    print -1 if n&1 else DFS_Iterative(1)
main()
