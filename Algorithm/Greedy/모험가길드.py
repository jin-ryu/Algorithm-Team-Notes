# 오름차순으로 정렬되어 있다고 가정할 때, 최소한의 그룹을 만듦
def solution(N, percent):
    count = 1
    group = []

    percent.sort()  # 오름차순 정렬

    for index in range(N):
        # 현재 그룹에 포함된 모험가의 수'가 '현재 확인하고 있는 공포도'보다 크거나 같다면 이를 그룹으로 설정
        if not group or percent[index] >= len(group):
            group.append(percent[index])
        else:
            group = []  # 다음 그룹
            count += 1

    return count

# 정답 코드
def answer():
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()

    result = 0  # 총 그룹의 수
    count = 0   # 현재 그룹에 포함된 모험가의 수

    for i in data:  # 공포도를 낮은 것부터 하나씩 확인하며
        count += 1  # 현재 그룹에 해당 모험가를 포함시키기
        if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
            result += 1 # 총 그룹의 수 증가시키기
            count = 0 # 현재 그룹에 포함된 모험가의 수 초기화
    
    print(result)


print(solution(5, [2, 3, 1, 2, 2]))  # 2
answer()