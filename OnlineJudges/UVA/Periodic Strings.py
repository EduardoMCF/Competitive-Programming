def main():
    from sys import stdin,stdout
    read,write = stdin.readline,stdout.write

    def zFunction(string):
        n = len(string)
        zArray = [0]*n
        l = r = 0
        for i in range(1,n):
            if i <= r:
                zArray[i] = min(r - i + 1, zArray[i-l])
            while i + zArray[i] < n and string[zArray[i]] == string[i + zArray[i]]:
                zArray[i] += 1
            if i + zArray[i] - 1 > r:
                l = i
                r = i + zArray[i] - 1

        return zArray

    n = int(read())
    ans = []
    for _ in range(n):
        read()
        string = read().strip()
        length = len(string)
        res = list(filter(lambda t: t[0] and not t[1]%t[0] and sum(t)==length,enumerate(zFunction(string))))
        ans.append('%i\n' %(length if not res else res[0][0]))
    write('\n'.join(ans))

main()
