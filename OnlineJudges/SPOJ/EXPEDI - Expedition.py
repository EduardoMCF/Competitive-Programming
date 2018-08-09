from sys import stdin,stdout
from heapq import heappush
n = input()
for i in xrange(n):
    t,heap,TP = input(),[],0
    for j in xrange(t):
        x,y = map(int,stdin.readline().split())
        TP += y
        heappush(heap,(-y,x))
    heappush(heap,(1000,-1))
    print heap
    L,P = map(int,stdin.readline().split())
    print L,TP
    if TP + P < L: stdout.write('-1\n')
    else:
        CA,S = P+1,0
        while True:
            for i in xrange(len(heap)):
                if CA >= heap[i][1]:
                    CA += abs(heap[i][0])
                    S += 1
                    heap[i] = (0,0)
                    break
            else:
                if CA >= L:
                    print S
                    break
                else:
                    print -1
                    break
            if CA >= L:
                print S
                break
    print heap


