positivos = 0
negativos = 0
pares = 0

for i in range(5):
    num = int(raw_input())
    if num > 0:
        positivos += 1
    if num < 0:
        negativos += 1
    if num % 2 == 0:
        pares += 1

print pares,'valor(es) par(es)'
print 5-pares,'valor(es) impar(es)'
print positivos,'valor(es) positivo(s)'
print negativos,'valor(es) negativo(s)'