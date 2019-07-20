from sys import stdin, stdout
r,w = stdin.readline,stdout.write

n,m = map(int,r().split())
problems = map(int,r().split())
probsQnt = [0]*n;probs = set();check = [False]*n;ans = []

for problem in problems:
    if problem not in probs: probs.add(problem)
    probsQnt[problem-1] += 1
    if len(probs) == n:
        for i in xrange(n):
            if not check[i]:
                probsQnt[i] -= 1
        check = [False]*n
        probs = set()
        ans.append('1')
        for i in xrange(n):
            if probsQnt[i] > 0:
                probsQnt[i] -= 1
                check[i] = True
                probs.add(i+1)
    else: ans.append('0')
w(''.join(ans))
