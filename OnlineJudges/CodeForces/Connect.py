from sys import stdin,stdout,setrecursionlimit
r,w = stdin.readline,stdout.write
setrecursionlimit(100000)
class Point:
  def __init__(self,x,y):
      self.x = x
      self.y = y

  def __xor__(self,other):
      return (self.x - other.x)**2 + (self.y - other.y)**2

def dfs(P,seen):
  if not (0 <= P.x < n and 0 <= P.y < n) or m[P.x][P.y] == '1': return
  if (P.x,P.y) in seen: return
  seen.add((P.x,P.y))
  dfs(Point(P.x+1,P.y),seen)
  dfs(Point(P.x-1,P.y),seen)
  dfs(Point(P.x,P.y+1),seen)
  dfs(Point(P.x,P.y-1),seen)
  return seen

n = int(r())
start = Point(*map(lambda x: int(x)-1,r().split()))
end = Point(*map(lambda x: int(x)-1,r().split()))
m = [r().strip() for _ in xrange(n)]
seen1,seen2 = set(),set()
seen1,seen2 = dfs(start,seen1),dfs(end,seen2)
if len(seen1) < len(seen2):
  if (end.x,end.y) in seen1: w('0'),exit()
else:
  if (start.x,start.y) in seen2: w('0'),exit()

w(str(min(Point(*i)^Point(*j) for i in seen1 for j in seen2)))
