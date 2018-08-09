n = int(raw_input())
saida = ''
for i in range(n):
    x = int(raw_input())
    if x % 2 == 0 and x != 0:
        saida += 'EVEN '
    if x % 2 != 0:
        saida += 'ODD '
    if x > 0:
        saida += 'POSITIVE'
    if x < 0:
        saida += 'NEGATIVE'
    if x == 0:
        saida = 'NULL'
    print saida
    saida = ''
