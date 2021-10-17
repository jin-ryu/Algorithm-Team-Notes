arr = input()
stack = []
isCorrect = True

for i in range(len(arr)):
    if arr[i] == '(' or arr[i] == '[':
        stack.append(arr[i])
    elif stack and stack[-1] == '(' and arr[i] == ')' :
        stack.pop()
        stack.append(2)
    elif stack and stack[-1] == '[' and arr[i] == ']':
        stack.pop()
        stack.append(3)    
    else:
        tmp = 0
        while stack and stack[-1] != '(' and stack[-1] != '[':
            # 숫자인 동안 누적해서 합 구하기
            tmp += stack.pop()
            
        if stack and stack[-1] == '(' and arr[i] == ')' :
            stack.pop()
            stack.append(2 * tmp)
        elif stack and  stack[-1] == '[' and arr[i] == ']':
            stack.pop()
            stack.append(3 * tmp)
        else:
            isCorrect = False
            break
            
if isCorrect and '(' not in stack and '[' not in stack:
    print(sum(stack))
else:
    print(0)

