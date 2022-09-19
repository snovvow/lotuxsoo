// 오류 코드
import sys
input = sys.stdin.readline

oneline = input().rstrip()
S,E,Q = oneline.split() #HH:MM HH:MM HH:MM
S = int(''.join(S.split(':')))
E = int(''.join(E.split(':')))
Q = int(''.join(Q.split(':')))

student = {}
cnt = 0
while True:
  twoline = input().rstrip()
  if len(twoline) < 5: break
  time, nickname = twoline.split()
  time = int(''.join(time.split(':')))

  if time<S:
    student[nickname] = 1
  elif E<=time<=Q:
    if nickname in student:
      student[nickname] += 1 
      cnt += 1

print(cnt)
