# dfs 탐색 
n = int(input()) # 컴퓨터 수 
m = int(input()) # 간선
graph = [[0]*(n+1) for _ in range(n+1)] # 인접리스트
done = [] # 바이러스 컴퓨터 

for _ in range(m):
    x,y = map(int,input().split())
    graph[x][y], graph[y][x] = 1,1
    
visited = [0]*(n+1)
def dfs(v): 
    done.append(v)
    for i in range(1, n+1):
        if (i not in done) and (graph[v][i]==1):
            dfs(i)

    return (len(done -1))

print(dfs(1))
