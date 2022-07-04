import sys
import re # 정규 표현식을 지원하는 re 모듈
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    t = str(input().rstrip("\n"))
    pattern = re.compile('(100+1+|01)+') # re.compile() 함수를 통해 ()안 패턴을 컴파일
    res = pattern.fullmatch(t) # pattern과 t가 매치되는지 확인

    if res:
        print('YES')
    else:
        print('NO')
