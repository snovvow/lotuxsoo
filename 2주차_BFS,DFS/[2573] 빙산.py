import sys
from collections import deque

def bfs(i,j,visit) :
    queue = deque([[i,j]]) # 큐를 [i,j]로 초기화
    melting_que = deque() # 빙하의 위치(i,j)와 인접한 바다 수를 저장
    visit[i][j] = 1 # 방문

# 인접한 모든 노드들에 대해 탐색 
    while queue :
        x,y = queue.popleft() 
        sea = 0 # 바다의 수
        for dx,dy in (-1,0), (1,0), (0,-1), (0,1):
            nx,ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and visit[nx][ny]==0:
                if graph[nx][ny] !=0: # 아직 탐색하지 않은 빙하
                    visit[nx][ny]=1
                    queue.append([nx,ny]) # 탐색 후 queue에 추가
                # 사방향 탐색 시 0일 경우 melt_cnt 증가
                else :
                    sea += 1
        if sea :
            melting_que.append([i,j,sea]) # (i,j)와 인접한 바다수 저장
            
    return melting_que

input=sys.stdin.readline
year = 0 # 답
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split()))) # 0~10 숫자가 배열로 입력

#반복문 종료 조건 -> 빙산의 갯수가 0이거나 2일 경우
while True :
    cnt = 0 # 빙산 개수를 담는 cnt 변수
    visit = [[0]*m for _ in range(n)] # 방문한 노드 체크 
    for i in range(n) :
        for j in range(m) :
            if graph[i][j] !=0 and visit[i][j]==0: # 아직 탐색하지 않은 빙하
                cnt += 1 # 빙산의 갯수 추가
                melt = bfs(i,j,visit) # 빙하가 녹는 위치(i,j)와 인접한 바다 수를 저장하는 큐
                
                while melt :
                    m_x, m_y, m = melt.popleft()
                    graph[m_x][m_y] = max(graph[m_x][m_y]-m, 0) # 빙하 깎기 

    # 빙산의 갯수가 0이거나 2일 경우 반복문 종료
    if cnt == 0 :
        year = 0
        break
    elif cnt >= 2 :
        break
    year += 1 # while 반복 한번에 1년
print(year)
