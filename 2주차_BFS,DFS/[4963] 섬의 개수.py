# 런타임에러 해결 문장 
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)
# 가로세로대각선 
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(x,y):
    jido[x][y]=0
    for i in range(8): # 상하좌우, 대각선 확인
        xx = x+dx[i]
        yy = y+dy[i]     
        if 0<=xx<h and 0<=yy<w and jido[xx][yy] == 1: # 땅이 이어지면 
            dfs(xx, yy)
            
while True:
    jido=[]
    w,h = map(int, input().split())
    if not w and not h: # 실행종료
        break
    for _ in range(h):
        jido.append(list(map(int, input().split()))) # 1->땅, 0-> 바다

    cnt = 0 # 섬 개수 

    for i in range(h):
        for j in range(w):
            if jido[i][j] == 1:
               dfs(i,j)
               cnt += 1
    print(cnt)
