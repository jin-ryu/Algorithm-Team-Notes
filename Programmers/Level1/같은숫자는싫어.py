def solution(arr):
    answer = [arr[0]]   # arr의 첫번째 값을 넣어줌
    for value in arr:
        # answer에 들어간 가장 최근 값과 값이 다를 경우 추가
        if answer and value != answer[-1]:
            answer.append(value)
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))