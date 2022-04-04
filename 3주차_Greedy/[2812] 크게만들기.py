import sys

N,K = map(int,sys.stdin.readline().split())
number = list(map(int,sys.stdin.readline().strip()))

stack = []
dN = K

for i in range(N):
  while dN>0 and stack and stack[-1] < number[i]:
    stack.pop()
    dN-=1
  stack.append(number[i])

for i in range(N-K):
    print(stack[i],end="")
