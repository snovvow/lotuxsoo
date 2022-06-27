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

# 입력받기
N = int(input())
parent = [0]*(N+1)

# 부모 테이블 상에서 부모를 자기자신으로 초기화
for i in range(1, N+1):
    parent[i]=i

# Union 연산 각각 수행
for i in range(N-2):
    a,b = map(int,input().split())
    union_parent(parent,a,b)

# find
res = []
for i in range(1,N+1):
    res.append(find_parent(parent,i))

# n개의 섬 중 하나의 부모노드만 다름 
# 부모 테이블 내용 출력
for i in range(1, len(res)):
    if res[i-1]!=res[i]:
        if res.count(res[i-1]) > res.count(res[i]):
            print(res[i-1],res[i])
            break
        else:
            print(res[i],res[i-1])
            break
