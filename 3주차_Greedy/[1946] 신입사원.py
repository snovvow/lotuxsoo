# 서류, 면접 중 하나라도 우수해야 뽑힌다.
# 신입사원의 최대 인원수 구하기 

t = int(input)
for _ in range(t):
  arr = [] 
  n = int(input())
  for _ in range(n):
    paper, inter = map(int,sys.stdin.readline().split())
    arr.append([paper, inter])
    # [[3,2],[1,4] ...]

  arr.sort() # paper 기준으로 정렬, 
  
  ans=1 # paper 1등은 뽑힘
  
  # inter 기준으로 정렬해보자
  max = arr[0][1] # paper 1등의 inter 기준
  for i in range(1,n):
    if max > arr[i][1]: # 앞에꺼보다 작으면 뽑힘 
      max = arr[i][1]
      ans+=1

  print(ans)
