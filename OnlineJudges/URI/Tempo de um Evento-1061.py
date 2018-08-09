#EMCF

none, dia_i = raw_input().split()
hora_i,min_i,seg_i = map(int,raw_input().split(' : '))
none, dia_f = raw_input().split()
hora_f,min_f,seg_f = map(int,raw_input().split(' : '))

dia_i,dia_f = int(dia_i),int(dia_f)
cont = 0

if hora_i > hora_f:
    duracao_h = 24 - (hora_i - hora_f)
else:
    duracao_h = hora_f - hora_i

if min_i > min_f:
    duracao_h -= 1
    cont += 1
    duracao_min = 60 - (min_i - min_f)
else:
    duracao_min = min_f - min_i

if seg_i > seg_f:
    if min_i == min_f:
        cont += 1
        duracao_h -= 1
    duracao_min -= 1
    duracao_seg = 60 - (seg_i - seg_f)
else:
    duracao_seg = seg_f - seg_i

duracao_dias = dia_f - dia_i - cont
duracao_h %= 24
duracao_min %= 60
if dia_i == dia_f: duracao_dias = 0
print '%i dia(s)' %duracao_dias
print '%i hora(s)' %duracao_h
print '%i minuto(s)' %duracao_min
print '%i segundo(s)' %duracao_seg