# 추를 사용하여 측정할 수 없는 최소 무게
# 왜 틀렸지..
import sys
input = sys.stdin.readline

def find(weight,N):
  num = 1
  for x in range(1,N):  
    if weight[x]-num > 1:
      num += 1
      break  
    num += weight[x]   
  return num
  
N = int(input())
weight = list(map(int, input().split()))
weight.sort() # [1,1,2,3,6,7,30]

ans = 1
if weight[0] == 1:
  ans = find(weight,N)

print(ans)
