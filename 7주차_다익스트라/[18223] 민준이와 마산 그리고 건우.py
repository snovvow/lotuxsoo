import sys
import heapq
input = sys.stdin.readline
INF= int(1e9) 
# V번:마산 / E: 간선개수 / P번:건우
V,E,P = map(int, input().split())

# 각 노드에 연결된 노드의 정보를 담는 리스트
graph = [[] for _ in range(V+1)]

for _ in range(E):
    # a->b로 가는 비용이 c
    a,b,c = map(int, input().split())
    # 양방향 노드
    graph[a].append([b,c])
    graph[b].append([a,c])

def dijk(s,e):
    distance = [INF for _ in range(V+1)]
    distance[s]=0
    q=[]
    heapq.heappush(q, (0,s)) # 시작노드로 가는 최단경로는 0
    while q:
        # 가장 최단거리가 짧은 노드 정보 꺼내기
        dist,now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        
        # 현재노드와 연결된 다른 인접노드들을 확인
        for next, next_dist in graph[now]:
            cost = dist + next_dist 
            # 현재노드를 거쳐서 다른노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))
    return distance[e]

if dijk(1,V)==dijk(1,P)*dijk(P,V):
    print('SAVE HIM')
else: 
    print('GOOD BYE')
