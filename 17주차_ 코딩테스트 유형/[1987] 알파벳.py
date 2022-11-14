import sys

input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
ans = 0
visited = set()


def dfs(x, y, cnt):
  global ans
  ans = max(ans, cnt)
  visited.add(arr[x][y])

  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < R and 0 <= ny < C:
      if arr[nx][ny] not in visited:
        dfs(nx, ny, cnt + 1)

  visited.remove(arr[x][y])


dfs(0, 0, 1)
print(ans)
##시간초과
