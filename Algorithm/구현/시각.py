def solution(N):
    count = 0
    
    for hour in range(N+1):
        for minute in range(0, 60):
            for second in range(0, 60):
                if '3' in set(str(hour) + str(minute) + str(second)):
                    count += 1

    return count

print(solution(5))  # 11475