n = int(input())
stairs = []
for i in range(n):
    stairs.append(int(input()))
ans = [0]*n

if n>=1:
    ans[0]=stairs[0]

if n>=2:
    ans[1]= stairs[0]+stairs[1]

if n >=3:
    ans[2] = max(stairs[2]+stairs[1], stairs[2]+stairs[0])
    for i in range(3,n):
        ans[i] = max(ans[i-2]+stairs[i], ans[i-3]+stairs[i-1]+stairs[i])

print(ans[n-1])
