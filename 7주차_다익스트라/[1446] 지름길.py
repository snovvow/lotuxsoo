# 지름길은 일방통행, 거리의 최솟값 구하기
import sys
input = sys.stdin.readline

# 지름길 개수 N, 고속도로 길이 D
N,D = map(int, input().split())

short = [[] for _ in range(10001)]

# 지름길 입력받기 
for _ in range(N):
    # s->e로 가는 비용 l
    s,e,l = map(int, input().split())
    short[s].append([l,e])

# 최단거리 테이블 모두 초기화  
distance = [i for i in range(D+1)]

for i in range(D+1):
    if i != 0: 
        distance[i] = min(distance[i], distance[i-1]+1)
    for l,e in short[i]:
        # 기존거리 vs 지름길로 가는 거리
        if e<=D and distance[e] > l + distance[i]:
            distance[e] = l + distance[i]

print(distance[D])
