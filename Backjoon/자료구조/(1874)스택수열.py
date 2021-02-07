n = int(input())
arr = [int(input()) for _ in range(n)]

def stack_sequence():
    stack = []
    sequence = []
    result = True
    num = 1 # 스택에 삽입할 숫자

    for i in range(n):
        # i: arr 수열에서 현재 보고 있는 index
        while num <= arr[i]:
            # 현재 숫자랑 가장 가까워지게 스택에 삽입
            stack.append(num)
            sequence.append('+')
            num += 1

        if stack[-1] == arr[i]:
            # top과 현재 숫자가 같으면 스택에서 pop
            stack.pop()
            sequence.append('-')
        else:
            # 같지 않다면 수열 만드는 것은 불가능
            result = False
            break

    # 결과 출력
    if result:
        for j in sequence:
            print(j)
    else:
        print("NO")
        

stack_sequence()