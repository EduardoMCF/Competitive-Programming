def main():
    from sys import stdin,stdout
    from fractions import gcd
    w = stdout.write
    stdin.next()
    it,f = int,(lambda a,b: '%i' %((a-1)*(b-1)) if gcd(a,b) == 1 else '-1')
    w('\n'.join(f(*map(it,line.split())) for line in stdin))
main()
