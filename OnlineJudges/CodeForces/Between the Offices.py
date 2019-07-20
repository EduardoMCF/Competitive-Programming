n = input()
flights = raw_input()
atual = flights[0]
sf = fs = 0
for f in flights[1:]:
    if 'SF' == atual+f:
        sf += 1
    elif 'FS' == atual+f:
        fs += 1
    atual = f
print 'YES' if sf > fs else 'NO'
