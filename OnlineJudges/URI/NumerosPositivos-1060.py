#EMCF
positivos = 0
for i in xrange(6):
    valor = float(raw_input())
    if valor > 0 : positivos += 1
print '%i valores positivos' %positivos