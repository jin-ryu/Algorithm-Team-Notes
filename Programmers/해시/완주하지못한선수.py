import collections

# 내가 푼 방법
def solution(participant, completion):
    # 참가자와 완주자 리스트를 합쳐 빈도수 체크
    counter = collections.Counter(participant + completion)
    
    # 빈도수가 홀수이면 완주하지 못한 선수
    for key, value in counter.most_common():
        if value % 2 == 1:
            return key

# 해결 방법1
def solution1(participant, completion):
    # 완주하지 못한 사람의 이름을 뽑아냄
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# 해결 방법2
def solution2(participant, completion):
    # 이름을 정렬
    completion.sort()
    participant.sort()

    for i in range(len(completion)):
        # 정렬된 순서가 맞지 않은 이름을 찾으면 완주히지 못한 사람
        if participant[i] != completion[i]:
            return participant[i]
    
    # 반복문을 도는 동안 찾지 못했다면, 마지막 사람이 완주하지 못한 사람
    return participant[-1]
        

participant1 = ['leo', 'kiki', 'eden']
completion1 = ['eden', 'kiki']
print(solution(participant1, completion1))

participant2 = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
completion2 = ['josipa', 'filipa', 'marina', 'nikola']
print(solution1(participant2, completion2))

participant3 = ['mislav', 'stanko', 'mislav', 'ana']
completion3 = ['stanko', 'ana', 'mislav']
print(solution2(participant3, completion3))

