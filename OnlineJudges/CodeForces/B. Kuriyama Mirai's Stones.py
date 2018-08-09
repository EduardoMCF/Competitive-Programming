from sys import stdin, stdout


def sum_a():
    soma = [[0]] + [[]]*n
    for i in xrange(1, n):
        soma[i] = soma[i-1] + nums[i-1]


n = input()
nums = map(int, stdin.readline().split())
t = input()
soma = sum_a()
soma_o = soma.sort(reverse=True)
for i in xrange(t):
    m, l, r = map(int, stdin.readline().split())
    if m == 1:
        stdout.write(str(soma[r]-soma[l])+'\n')
    else:
        stdout.write(str(soma_o[r]-soma_o[l]+'\n'))
