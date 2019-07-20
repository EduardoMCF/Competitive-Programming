from sys import stdin,stdout
r,w = stdin.readline,stdout.write

class SparseTable:
    def __init__(self,array,func):
        self.array = array
        self.func = func
        self.log = self._logPreprocess()
        self.sparseTable = self._preprocess()

    def _logPreprocess(self):
        n = len(self.array); log = [0] * (n+1)
        for i in range(2,n+1):
            log[i] = log[i//2] + 1
        return log

    def _preprocess(self):
        n = len(self.array); k = self.log[n]+1
        sTable = [[0]*(k+1) for i in xrange(n+1)]

        for i in xrange(n):
            sTable[i][0] = self.array[i]

        for j in xrange(1,k+1):
            for i in xrange(n+1):
                if i + (1 << j) > n: break
                sTable[i][j] = self.func(sTable[i][j-1], sTable[i + (1 << (j-1))][j-1])

        return sTable

    def __len__(self):
        return len(self.array)

    def __getitem__(self,interval):
        l,r = (0,interval) if isinstance(interval,int) else (interval.start if interval.start else 0,interval.stop if interval.stop else len(self.array)-1)
        j = self.log[r-l+1]
        return self.func(self.sparseTable[l][j], self.sparseTable[r-(1 << j)+1][j])


    def __str__(self):
        return '\n'.join(' '.join(map(str,row)) for row in self.sparseTable)


n = int(r())
st = SparseTable(list(map(int,r().split())),min)
for _ in range(int(r())):
    L,R = map(int,r().split())
    w('%i\n' %st[L:R])
