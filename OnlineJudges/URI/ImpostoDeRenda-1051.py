#EMCF

renda = float(raw_input())
isento = True
if renda - 2000 > 0:
    renda -= 2000
    isento = False
    if renda - 1000 > 0:
        renda -= 1000
        imposto = 1000 * 0.08
        if renda - 1500 > 0:
            renda -= 1500
            imposto += (1500 * 0.18)
            if renda > 0:
                imposto += (renda * 0.28)
        else:
            imposto += renda * 0.18
    else:
        imposto = renda * 0.08

if isento == True:
    print 'Isento'
else:
    print 'R$ %.2f' %imposto

