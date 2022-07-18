import sys
input = sys.stdin.readline

# 행렬곱셈
def gop(n,mat1,mat2):
  res = [[0 for _ in range(n)] for _ in range(n)]

  for i in range(n):
    for j in range(n):
      for k in range(n):
        res[i][j] += mat1[i][k]*mat2[k][j] 
      res[i][j] %= 1000

  return res

# 분할
def devide(n,b,mat):
  if b==1:
    return mat
  elif b==2:
    return gop(n,mat,mat)
  else:
    tmp = devide(n,b//2,mat)
    if b%2==0:
      return gop(n,tmp,tmp)
    else:
      return gop(n,gop(n,tmp,tmp),mat)

n,b = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
result = devide(n,b,a)

for r in result:
  for i in r:
    print(i%1000, end=' ')
  print()
