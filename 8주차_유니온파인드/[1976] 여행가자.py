import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트노드를 찾을 때까지 재귀호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x # 루트노드

# 두 원소가 속한 집합 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력
N = int(input())
M = int(input())
parent = [0]*(N+1)

for i in range(1,N+1):
    parent[i] = i

for i in range(1, N+1):
    graph = list(map(int, input().split()))
    for j in range(1, len(graph)+1):
        if graph[j-1] == 1: 
            union_parent(parent, i, j)

plan = list(map(int,input().split()))
res = []
for i in plan:
    res.append(find_parent(parent,i))

if len(set(result)) == 1:
    print("YES")
else:
    print("NO")
