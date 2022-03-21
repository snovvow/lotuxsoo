n,k = map(int, input().split()) #n개의 종류의 동전으로 k원 만들기 
m = [] #동전가치 저장
for _ in range(n):
    m.append(int(input()))

ans = [0 for i in range(k+1)] #동전의 합이 1<=i<=k이 되는 경우의 수 저장
ans[0] = 1
for i in m:
    for j in range(1, k+1):
        if j-i >= 0:
            ans[j] += ans[j-i] 
        
print(ans[k])
