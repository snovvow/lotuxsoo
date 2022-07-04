string = input()
stack = [] 

for i in range(len(string)):
  stack.append(string[i])
  if stack[-4:]==["P","P","A","P"]:
    for _ in range(3):
      stack.pop()

if stack==["P","P","A","P"] or stack==["P"]:
  print("PPAP")
else:
  print("NP")
