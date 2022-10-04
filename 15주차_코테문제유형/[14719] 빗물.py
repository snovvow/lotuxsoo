import sys
input = sys.stdin.readline

n, m = map(int, input().split())
height = list(map(int,input().split()))

l,r = 0, len(height)-1
l_max, r_max = height[l], height[r]
ans = 0
while l < r:
  l_max = max(l_max, height[l])
  r_max = max(r_max, height[r])

  if l_max <= r_max:
    ans += l_max - height[l]
    l += 1
  else:
    ans += r_max - height[r]
    r -= 1

print(ans)
