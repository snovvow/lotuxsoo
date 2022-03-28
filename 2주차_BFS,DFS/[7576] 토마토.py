# BFS 이용
from  collections import deque

m, n =map(int, input().split())
box = []
for _ in range(n):
    box.append(list(map(int, input().split()))) # 1: 익토/ 0: 안익토/ -1: x
queue= deque([]) # 빈 리스트 추가 

def bfs(): # 재귀x
    while queue:
        x,y = queue.popleft()
        for dx,dy in (-1,0), (1,0), (0,-1), (0,1):
            nx, ny = x+dx, y+dy

            if 0<=nx<n and 0<=ny<m and box[nx][ny]==0:
                # 익토로 만들고 큐에 추가 
                box[nx][ny]=box[x][y]+1
                queue.append([nx,ny]) 

for i in range(n):
    for j in range(m):
        if box[i][j]==1: # 익토 queue에 추가
            queue.append([i,j])  

bfs()

ans = 0 # 토마토가 모두 익는 최소 날짜

for i in box:
    for j in i:
        if j==0: # 안익은거 있을 때
            print(-1)
            exit(0)
    # 다 익혔으면 답은 최댓값 
    ans = max(ans, max(i))
print(ans-1) # 처음을 1로 시작했으므로 
