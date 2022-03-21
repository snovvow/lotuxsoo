n,m = map(int, input().split())
table = []
for _ in range(n):
    table.append(list(map(int, list(input().rstrip()))))
ans = 0
dp = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if table[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        ans = max(dp[i][j], ans)
 
print(ans*ans)
