import sys

input = sys.stdin.readline
 
n = int(input()) 
data = list(map(int,input().split())) 

#최대값 저장 변수
ans=0

#i번째 원소까지의 누적합
sum=[] 
sum.append(data[0]) 

for i in range(1,n): 
    sum.append(sum[i-1]+data[i]) 

for i in range(1,n-1): 
    ans=max(ans,sum[n-2]+sum[i-1]-data[i])

for i in range(1, n-1): 
    ans = max(ans, sum[n-1] - data[0] - data[i] + sum[n-1] - sum[i]) 

for i in range(1,n-1): 
    ans=max(ans,sum[n-2] - data[0] + data[i])
       
print(ans)
