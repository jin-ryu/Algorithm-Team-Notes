# 내가 푼 방법 (인터넷 참고함)
def solution(numbers, target):
    a = [0]    

    for i in numbers:
        b = []  
        for j in a:
            b.append(j+i)
            b.append(j-i)
        a=b
      
    return a.count(target)

# 해결 방법 1 - 이해하는 중
def solution1(numbers, target):
    print(numbers, target)
    if not numbers and target == 0 :    # 리스트가 비어있고 target이 0인 경우 
        return 1
    elif not numbers:                   # 리스트가 비어있는 경우 (재귀 종료)
        return 0
    else:
        return solution1(numbers[1:], target - numbers[0]) + solution1(numbers[1:], target + numbers[0])
    

numbers = [1,1,1,1,1]
target = 3

print(solution(numbers, target))
print(solution1(numbers, target))