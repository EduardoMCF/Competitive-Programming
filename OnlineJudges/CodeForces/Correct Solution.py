n = map(int,list(raw_input()))
guess = raw_input()
mini = min(n, key = lambda x: x if x else 10)
n.remove(mini)
zeros = 0
while 0 in n:
    zeros+=1
    n.remove(0)
res = '%i%s%s' %(mini,zeros*'0',''.join(map(str,sorted(n))))
print "OK" if res == guess else "WRONG_ANSWER"
