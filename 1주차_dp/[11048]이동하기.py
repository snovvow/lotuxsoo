y,x = map(int, input().split()) 
m = []
for i in range(y):
    m.append(list(map(int, input().split())))

ans = [[0]*(x+1) for i in range(y+1)]

for i in range(1, y+1): 
    for j in range(1, x+1):
        ans[i][j] = m[i-1][j-1] + max(ans[i-1][j], ans[i][j-1], ans[i-1][j-1])

print(ans[i][j])
