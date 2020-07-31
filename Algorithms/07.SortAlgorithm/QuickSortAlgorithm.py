# Quick Sort
# 분할 정복(Divide and Conquer) 기법과 재귀 알고리즘 이용
# pivot을 기준으로 작은 그룹, 큰 그룹으로 분할 
# 이 과정을 각 그룹에서 반복

# 재귀 형식
def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    # 중간 값을 pivot으로 설정
    pivot = numbers[len(numbers) // 2]

    # 그룹 리스트
    lesser_numbers, equal_numbers, greater_numbers = [], [], []

    # 그룹 분할
    for num in numbers:
        if num < pivot:
            lesser_numbers.append(num)
        elif num > pivot:
            greater_numbers.append(num)
        else:
            equal_numbers.append(num)

    # 재귀 호출 (각 그룹에서 그룹 분할 반복)
    return quick_sort(lesser_numbers) + equal_numbers+ quick_sort(greater_numbers)

# 비재귀형식 (모든 재귀함수는 반복문으로 구현하는 것이 가능)
# 재귀함수 보다는 반복문이 더 좋은 퍼포먼스를 얻을 수 있다
# stack을 이용해 partition의 반환값을 비교해 아직 부분집합의 크기가 1보다 크다면
# stack에 넣어 반복문을 수행시킬 수 있음
def partition(list, start, end):
    pivot = list[start]
    left = start + 1
    right = end

    # left는 리스트의 시작, right는 끝 인덱스를 가짐
    # left에는 pivot보다 작은 값, right에서는 pivot보다 큰 값을 둔다
    # left와 right가 교차되면 (left > right) 정렬 완료
    while True:
        while left <= right and list[left] <= pivot:
            left += 1
        while left <= right and list[right] > pivot:
            right -= 1

        # 종료 조건
        if left > right:
            break
        # 종료 조건에 맞지 않다면 swap 후 다시 반복
        else:
            list[left], list[right] = list[right], list[left]
     
    # pivot 변경
    list[start], list[right] = list[right], list[start]
    return right

            
def quick_sort2(numbers):
    stack = []
    start = 0
    end = len(numbers)-1

    stack.append(start)
    stack.append(end)

    while stack:
        end = stack.pop()
        start = stack.pop()
        pivot = partition(numbers, start, end)
        print(pivot)

        # 체크 안한 pivot이 있다면 추가 (start, end로 추가)
        if pivot-1 > start:
            stack.append(start)
            stack.append(pivot-1)
        if pivot+1 < end:
            stack.append(pivot+1)
            stack.append(end)

        print(stack)

    return numbers

numbers = [3, 30, 34, 5, 9]
print(quick_sort2(numbers))