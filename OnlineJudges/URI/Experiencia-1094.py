n = int(raw_input())
total,C,R,S = 0,0,0,0
for i in range(n):
    num, tipo = raw_input().split()
    num = int(num)
    total += num
    if tipo == 'C':
        C += num
    if tipo == 'R':
        R += num
    if tipo == 'S':
        S += num
porc_C = float(C)/total * 100
porc_R = float(R)/total * 100
porc_S = float(S)/total * 100
print 'Total: %i cobaias' %total
print 'Total de coelhos: %i' %C
print 'Total de ratos: %i' %R
print 'Total de sapos: %i' %S
print 'Percentual de coelhos: %.2f %%' %porc_C
print 'Percentual de ratos: %.2f %%' %porc_R
print 'Percentual de sapos: %.2f %%' %porc_S