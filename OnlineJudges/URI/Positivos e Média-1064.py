cont = 0
lista = []
for i in xrange(6):
    num = float(raw_input())
    if num > 0:
        cont += 1
        lista.append(num)

media = sum(lista)/len(lista)
print '%i valores positivos' %cont
print '%.1f' %media