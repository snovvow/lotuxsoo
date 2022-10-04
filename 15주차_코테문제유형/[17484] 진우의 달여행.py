import sys

input = sys.stdin.readline
n, m = map(int, input().split())
mat = []
for _ in range(n):
  mat.append(list(map(int, input().split())))
MAX_VAL = 1e9
dp = [[[MAX_VAL] * 3 for _ in range(m)] for _ in range(n)]

for x in range(n):
  for y in range(m):
    if x == 0:
      for i in range(3):  #0->오대위 1->위 2->왼대위
        dp[x][y][i] = mat[x][y]
    else:
      if y == 0:  # 왼대위(2)x
        dp[x][y][0] = min(dp[x - 1][y + 1][1], dp[x - 1][y + 1][2]) + mat[x][y]
        dp[x][y][1] = dp[x - 1][y][0] + mat[x][y]
      elif y == m - 1:  # 오대위(0)x
        dp[x][y][1] = dp[x - 1][y][2] + mat[x][y]
        dp[x][y][2] = min(dp[x - 1][y-1][0], dp[x - 1][y-1][1]) + mat[x][y]
      else:  # 가운데들
        dp[x][y][0] = min(dp[x - 1][y + 1][1], dp[x - 1][y + 1][2]) + mat[x][y]
        dp[x][y][1] = min(dp[x - 1][y][0], dp[x - 1][y][2]) + mat[x][y]
        dp[x][y][2] = min(dp[x - 1][y - 1][0], dp[x - 1][y - 1][1]) + mat[x][y]

ans = MAX_VAL
for i in range(m):
  ans = min(min(dp[n - 1][i]), ans)
print(ans)
