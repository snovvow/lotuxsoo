import sys
input = sys.stdin.readline
## 투포인터 알고리즘
N,K = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0,0
check = [0]*100001
ans = 0

while right < N:
  if check[arr[right]] < K:
    check[arr[right]] += 1
    right += 1
  else:
    check[arr[left]] -= 1
    left += 1
  ans = max(ans, right-left)

print(ans)
