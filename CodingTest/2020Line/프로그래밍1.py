import numpy as np
import collections

def solution(boxes):
    answer = 0
    box_count = 0   # 짝이 맞은 박스 개수
    N = len(boxes)  # 전체 박스 개수

    boxes = np.array(boxes).flatten().tolist()  # 2차원배열 -> 1차원
    counter = dict(collections.Counter(boxes))  # 리스트 요소와 개수를 딕셔너리로 표현

    for count in counter.values():    # 개수가 홀수 인 것 만큼 추가 구매를 하면 됨
        box_count += count // 2
            
    if box_count >= N: # 가지고 있는 박스를 다 사용한 경우
        return answer

    while box_count < N:    # 박스를 다 사용할때까지 추가 구매로 짝을 맞춤
        answer += 1
        box_count += 1  

    return answer

print(solution([[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]))
print(solution([[1, 2], [3, 4], [5, 6]]))
print(solution([[1, 2], [2, 3], [3, 1]]))
