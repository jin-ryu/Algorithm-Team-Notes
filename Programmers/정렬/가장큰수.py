import functools

# 해결 방법1
def solution(numbers):
    numbers = list(map(str, numbers))
    # 문자열로 표현된 숫자를 곱하여 같은 패턴을 갖게함
    # 1000이하의 숫자만 들어오기 때문에 * 3
    numbers.sort(key=lambda x: x*3, reverse=True)

    # str(int())를 해줘야 통과되는데 이유는 모르겠음
    return str(int("".join(numbers)))

# 해결 방법2
def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))    #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution1(numbers):
    n = [str(x) for x in numbers]
    
    # 나만의 숫자 비교 방법을 key로 정렬 custom
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer 

numbers = [6, 10, 2]
numbers2 = [3, 30, 34, 5, 9]

print(solution(numbers))
print(solution1(numbers2))