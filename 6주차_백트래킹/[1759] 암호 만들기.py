import sys 
from itertools import combinations 
input = sys.stdin.readline

L,C = map(int, input().split())
alpha = list(map(str, input().split()))

# 정렬된 배열을 유지할것
alpha.sort()
# 최소 한개의 aeiou, 최소 두개의 자음이 쓰일것
m_alpha = ['a', 'e', 'i', 'o','u']
com = combinations(alpha, L)

for c in com:
    m_cnt = j_cnt = 0
    for i in range(L):
        if c[i] in m_alpha:
            m_cnt += 1
        else: # 자음
            j_cnt += 1

    if m_cnt>=1 and j_cnt>=2:
        print(''.join(c))
