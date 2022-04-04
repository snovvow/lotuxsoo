N = int(input())
# 소가 도착한 시간, 검문 시간은 소마다 다르다
# 모든 소가 입장하는 최소시간 구하기
# 앞 소-> 5초 도착+7초 검문 / 뒷 소->8초 도착+4초 기다림+x초 검문

time = []
for _ in range(N):
  time.append(list(map(int, input().split())))
  # 리스트 or 튜플..?
  #[[2,1],[8,3],[5,7]]

time.sort()
ans =0
for i in time:
  if ans < i[0]: # n-1번 말 끝나기 전 도착
    ans= i[0]+i[1]
  else: # ans >= i[0] n-1번 말 끝나고 도착
    ans= ans+i[1]

print(ans)
