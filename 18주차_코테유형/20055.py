#골드5
import sys
input = sys.stdin.readline
from collections import deque

N,K = map(int,input().split())
A = deque(list(map(int,input().split()))) #내구도
robot = deque([0] * N)
ans = 0

while True:
    A.rotate(1)
    robot.rotate(1)
    robot[-1]=0
    
    if sum(robot):
        for i in range(N - 2, -1, -1): # N-2~0
            if robot[i] == 1 and robot[i+1] == 0 and A[i+1]>=1:
                robot[i+1] = 1
                robot[i] = 0
                A[i+1] -= 1
        robot[-1] = 0
    
    if robot[0] == 0 and A[0]>=1:
        robot[0] = 1
        A[0] -= 1
    ans += 1
    
    # 종료
    if A.count(0) >= K:
        break

print(ans)
