import sys
input = sys.stdin.readline

N,d,k,c = map(int, input().split())
chobab = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

s,e = 0,0
ans = 0

while s != N:
  e = s + k
  case = set()
  flag = 0
  
  for i in range(s,e):
    i %= N
    case.add(chobab[i])
    if chobab[i] == c:
      flag = 1
  cnt = len(case)
  if flag == 0: cnt += 1
  ans = max(ans, cnt)
  s += 1

print(ans)
