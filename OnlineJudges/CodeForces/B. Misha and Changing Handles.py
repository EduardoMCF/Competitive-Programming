n = int(raw_input())
nomes,semon={},{}
for i in xrange(n):
    vel,nov = raw_input().split()
    if vel not in nomes.keys() and vel not in nomes.values(): nomes[vel],semon[nov] = nov,vel
    else:
        nomes[semon[vel]] = nov
        semon[nov] = semon[vel]
        del semon[vel]
print len(nomes)
for i in nomes.keys(): print i, nomes[i]