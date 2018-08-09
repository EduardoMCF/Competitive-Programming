# EMCF
# coding: utf-8
### ENTRADA
horarios = map(int,raw_input().split())
duracao_h = 0
duracao_min = 0

### LÓGICA
if horarios[0] < horarios[2]:
    duracao_h = horarios[2] - horarios[0]
else:
    duracao_h = 24-(horarios[0]-horarios[2])

if horarios[1] > horarios[3]:
    duracao_h -= 1
    duracao_min = 60 - (horarios[1] - horarios[3])
else:
    duracao_min = horarios[3] - horarios[1]

### SAÍDA

print 'O JOGO DUROU %i HORA(S) E %i MINUTO(S)' %(duracao_h,duracao_min)