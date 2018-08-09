s = raw_input()
if '1' in s:
    p1=s.index('1')
    j = s[p1:]
    if j.count('0') >= 6: print 'yes'
    else: print 'no'
else:print 'no'