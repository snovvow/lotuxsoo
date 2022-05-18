# 부등호를 만족한느 k+1자리 정수중에서 최대, 최솟값 찾기
# 모두 다른 숫자가 선택되야 함.

def good (x,y, op): #num[index-1], str(i), a[index-1]
    if op == '<':
        if x>y:
            return False
    elif op == '>':
        if x<y:
            return False
    return True

def rec(index, num):
    if index == n+1:
        ans.append(num)
        return 

    for i in range(10): # 0~9
        if check[i]: 
            continue 
        if index==0 or good(num[index-1], str(i), a[index-1]): 
            check[i] = True
            rec(index+1, num+str(i)) # 재귀
            check[i] = False


n = int(input())
a = input().split()
ans = []
check = [False]*10 # 해당 숫자 사용했는지 안했는지 체크
rec(0, '')
ans.sort()
print(ans[-1])
print(ans[0])
