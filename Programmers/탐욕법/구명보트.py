def solution(people, limit):
    answer = 0
    max_idx = len(people)-1     # 구출되지 못한 최대 무게의 인덱스
    min_idx = 0     # 구출되지 못한 최소 무게의 인덱스
    
    people.sort()
    left = limit - people[max_idx]  # 여유 무게

    while min_idx <= max_idx :
        # 한 사람만 남은 경우
        if min_idx == max_idx:
            answer += 1
            break 
        
        # 여유 무게보다 덜 나가는 사람이라면 태움
        if people[min_idx] <= left:
            left -= people[min_idx]
            min_idx += 1
        else:
            max_idx -= 1
            left = limit - people[max_idx]  # 새로운 배에는 제일 무게가 많이 나가는 사람부터 태움
            answer += 1     # 배 보냄

    return answer


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([20, 10, 10, 10, 50, 70, 80, 50], 100))
print(solution([10, 10, 20, 50, 20], 100))