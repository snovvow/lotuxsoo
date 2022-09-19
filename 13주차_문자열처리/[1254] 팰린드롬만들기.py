import sys
input = sys.stdin.readline

def Palindrome() : 
  for i in range(len(s)):
    tmp = s + s[:i][::-1]
    print(tmp)
    if tmp == tmp[::-1] :
      print(len(tmp))
      break

s = input().rstrip()
Palindrome()
