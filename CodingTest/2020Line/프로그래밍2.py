def solution(ball, order):
    answer = []
    start = 0   # 파이프의 왼쪽 끝
    end = len(ball)-1   # 파이프의 오른쪽 끝
    wait = []  # 명령을 바로 실행하지 못한 경우 대기 

    for num in order:
        # 대기하는 공이 뺄 수 있는 조건이 되면 다음 조건보다 우선
        while True:
            if ball[start] in wait:   # 대기하는 공을 왼쪽에서 꺼낼 수 있는 경우
                answer.append(ball[start])
                wait.remove(ball[start])
                start += 1
            elif ball[end] in wait:    # 대기하는 공을 오른쪽에서 꺼낼 수 있는 경우
                answer.append(ball[end])
                wait.remove(ball[end])
                end -= 1
            else:   # 대기하는 공을 뺄 수 없는 경우
                break

        if num == ball[start]:  # 파이프의 왼쪽 끝에 공이 있는 경우
            answer.append(ball[start])
            start += 1
        elif num == ball[end]:  # 파이프의 오른쪽 끝에 공이 있는 경우
            answer.append(ball[end])
            end -= 1
        else:   # 파이프에 양끝에 공이 없는 경우
            wait.append(num)
            
    return answer


print(solution([1, 2, 3, 4, 5, 6], [6, 2, 5, 1, 4, 3]))
print(solution([11, 2, 9, 13, 24], [9, 2, 13, 24, 11]))
print(solution([1, 2, 3, 4, 5], [3, 2, 4, 1, 5]))