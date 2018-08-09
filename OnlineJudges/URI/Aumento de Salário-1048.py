#EMCF
# coding:utf-8

salario = float(raw_input())
novo_salario = 0

if salario <= 400.00:
    novo_salario = salario * 1.15
    reajuste = salario * 0.15
    percentual = 15

elif 400.01 <= salario <= 800.00:
    novo_salario = salario * 1.12
    reajuste = salario * 0.12
    percentual = 12

elif 800.01 <= salario <= 1200.00:
    novo_salario = salario * 1.10
    reajuste = salario * 0.10
    percentual = 10

elif 1200.01 <= salario <= 2000.00:
    novo_salario = salario * 1.07
    reajuste = salario * 0.07
    percentual = 7

elif salario > 2000.00:
    novo_salario = salario * 1.04
    reajuste = salario * 0.04
    percentual = 4

print "Novo salario: %.2f" %novo_salario
print "Reajuste ganho: %.2f" %reajuste
print "Em percentual: %i %%" %percentual
