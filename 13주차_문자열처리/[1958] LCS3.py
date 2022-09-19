import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
s3 = input().rstrip()
x = len(s1)
y = len(s2)
z = len(s3)

arr = [[[0] * (z+1) for _ in range(y+1)] for _ in range(x+1)]


for i in range(1, x+1):
    for j in range(1, y+1):
        for k in range(1, z+1):
            if s1[i-1] == s2[j-1] and s2[j-1] == s3[k-1]:
                arr[i][j][k] = arr[i-1][j-1][k-1] + 1
            
            else:
                arr[i][j][k] = max(arr[i][j][k-1], arr[i][j-1][k], arr[i-1][j][k])

print(arr[-1][-1][-1])
