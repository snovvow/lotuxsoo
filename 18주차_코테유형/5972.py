#골드5 다익스트라
import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, [0,start])
    while q:
        dis, now = heapq.heappop(q)
        if distance[now] < dis:
            continue
        for x,y in graph[now]:
            cost = dis + y
            if distance[x] > cost:
                heapq.heappush(q, [cost,x])
                distance[x] = cost

N,M = map(int,input().split()) #N개의 헛간, M개의 길
graph = [[] for _ in range(N+1)]
INF = int(1e9)
distance = [INF for _ in range(N+1)]

for _ in range(M):
    A,B,C = map(int,input().split())
    graph[A].append((B,C))
    graph[B].append((A,C))
dijkstra(1)

print(distance[N])
