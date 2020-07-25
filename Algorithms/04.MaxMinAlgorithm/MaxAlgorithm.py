#[?] 주어진 데이터 중에서 가장 큰 값
import sys

# 최댓값 알고리즘(Max Algorithm): (주어진 범위 + 주어진 조건)의 자료들의 가장 큰 값
def main():
    #[0] Initialize
    max_value = -sys.maxsize - 1             # 숫자 형식의 데이터 중 가장 작은 값으로 초기화

    #[1] Input
    numbers = [ -2, -5, -3, -7, -1 ]    # MAX: -1
    N = len(numbers)                    # 의사코드

    #[2] Process: MAX
    for i in range(0, N):               # 주어진 범위
        if numbers[i] > max_value:            # 더 큰 데이터가 있다면
            max_value = numbers[i]            # MAX: 더 큰 값으로 할당

    #[3] Output
    print('최댓값: {}'.format(max_value))

#[!] My code
def mycode1():
    numbers = [ -2, -5, -3, -7, -1 ]
    print('최댓값: {}'.format(max(numbers)))

def mycode2():
    numbers = [ -2, -5, -3, -7, -1 ]
    max_value =  numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    print('최댓값: {}'.format(max_value))

if __name__ == "__main__":
    main()
    mycode1()
    mycode2()



