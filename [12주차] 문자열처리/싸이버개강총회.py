import sys
input = sys.stdin.readline

S,E,Q = input().split()
S = int(S[:2]+S[3:]) 22:00 2200
E = int(E[:2]+E[3:])
Q = int(Q[:2]+Q[3:])
student = {}

while True:
  line = input().split()
  if len(line) < 5: break  
  time, name = line.split()
  time = int(time[:2]+time[3:])
  if time <= S:
    student[name] = 1
  elif E<=time<=Q:
    if name in student:
      student[name] += 1

ans = 0
for value in student.values():
  if value >= 2:
    ans += 1

print(ans)
