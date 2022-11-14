import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n) :
    a,b = map(int,input().split())
    lst.append([a,b]) 
lst.sort()

res = 0
# 가장 높은 기둥의 번호
i = 0
for box in lst:
  if box[1] > res: 
    res = box[1] # res에 높은기둥 길이
    idx = i # idx에 높은기둥 인덱스
  i += 1

# 앞에서부터
height = lst[0][1]

for i in range(idx): # 최대높이 전까지
  if height < lst[i+1][1]: # 다음기둥이 높으면
    res += height * (lst[i+1][0] - lst[i][0])
    height = lst[i+1][1]
  else: 
    res += height * (lst[i+1][0] - lst[i][0])

# 뒤에서부터
height = lst[-1][1]

for i in range(n-1, idx, -1):
  if height < lst[i-1][1]:
    res += height * (lst[i][0] - lst[i-1][0])
    height = lst[i-1][1]
  else:
    res += height * (lst[i][0] - lst[i-1][0])

print(res)
