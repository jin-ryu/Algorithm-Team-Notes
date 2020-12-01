def get_set(arr):
    # 대소문자 구분 없앰
    arr = arr.lower()
    set_arr = []
    for i in range(len(arr)-1):
        sub = arr[i:i+2]
        if sub.isalpha():
            # 알파벳인 sub string만 추가
            set_arr.append(sub)
    return set_arr
            
def solution(str1, str2):
    answer = 65536
    # 다중 집합 생성
    list1 = get_set(str1)
    list2 = get_set(str2)
    
    x = 0
    for i in set(list1):
        # 교집합의 개수 카운트
        x += min(list1.count(i), list2.count(i))
    y = len(list1) + len(list2) - x
    
    if x == 0 and y == 0:
        return answer
    
    return int((x/y)*answer)