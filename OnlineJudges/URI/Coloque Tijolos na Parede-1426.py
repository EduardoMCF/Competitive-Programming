n = raw_input()
for i in xrange(int(n)):
    m = [[0],[0,0],[0,0,0],[0,0,0,0],[0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    for i in xrange(0,9,2):
        e,c=map(int,raw_input().split()),0
        for j in xrange(0,i+1,2):
            m[i][j]=e[c]
            c+=1
    for i in xrange(0,8,2):
        for j in xrange(0,i+1,2):
            m[i+2][j+1]=(m[i][j]-m[i+2][j]-m[i+2][j+2])/2
            m[i+1][j],m[i+1][j+1]=m[i+2][j]+m[i+2][j+1],m[i+2][j+1]+m[i+2][j+2]
    for i in m:
        for j in xrange(len(i)):
            if j!=len(i)-1: print i[j],
            else:print i[j]