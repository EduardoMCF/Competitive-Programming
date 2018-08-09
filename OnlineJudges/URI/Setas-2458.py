from sys import stdin,stdout
from collections import deque
def backtrack(cord):
    stack, seen = deque(), set([cord])
    stack.appendleft(cord)
    insecures = 0
    while stack:
        row,col = stack.popleft()
        insecures += 1
        if (0,0) <= (row,col-1) <= (n-1,n-1) and m[row][col-1] == '>' and (row,col-1) not in seen: stack.appendleft((row,col-1)),seen.add((row,col-1))
        if (0,0) <= (row,col+1) <= (n-1,n-1) and m[row][col+1] == '<' and (row,col+1) not in seen: stack.appendleft((row,col+1)),seen.add((row,col+1))
        if (0,0) <= (row+1,col) <= (n-1,n-1) and m[row+1][col] == 'A' and (row+1,col) not in seen: stack.appendleft((row+1,col)),seen.add((row+1,col))
        if (0,0) <= (row-1,col) <= (n-1,n-1) and m[row-1][col] == 'V' and (row-1,col) not in seen: stack.appendleft((row-1,col)),seen.add((row-1,col))
    return insecures
n = input()
m,res = [stdin.readline() for i in xrange(n)],0
for i in xrange(n):
    if m[0][i] == 'A': res += backtrack((0,i))
    if m[n-1][i] == 'V': res += backtrack((n-1,i))
    if m[i][0] == '<': res += backtrack((i,0))
    if m[i][n-1] == '>': res += backtrack((i,n-1))
stdout.write(str(n**2-res)+'\n')