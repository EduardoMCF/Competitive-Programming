from math import pi,sin
n,r = map(int,raw_input().split())
print r/(2*sin((90-180./n)/180.*pi)/sin((360./n)/180.*pi)-1)
print ("\x18")