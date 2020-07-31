# 1번: 1,2,3,4,5, ...
# 2번: 2,1,2,3,2,4,2,5, ...
# 3번: 3,3,1,1,2,2,4,4,5,5, ...

# 내가 푼 방식
def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    counts = [0,0,0]     # 맞은 개수

    for i in range(len(answers)):
        if first[i%len(first)] == answers[i]:
            counts[0] += 1
        if second[i%len(second)] == answers[i]:
            counts[1] += 1
        if third[i%len(third)] == answers[i]:
            counts[2] += 1
    
    answer = [i+1 for i in range(3) if counts[i] == max(counts)]
    return list(answer)

# 해결 방법1
def solution1(answers):
    patterns = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    counts = [0] * len(patterns)

    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                counts[j] += 1
    return [i + 1 for i, count in enumerate(counts) if count == max(counts)]

answers1 = [1,2,3,4,5]
answers2 = [1,3,2,4,2]

print(solution(answers1))
print(solution1(answers2))