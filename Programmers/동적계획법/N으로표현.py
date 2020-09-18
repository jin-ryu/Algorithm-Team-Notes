# N을 가지고 number를 만드는 방법의 개수를 세자(X)
# N을 조합해서 만들 수 있는 수 중에 number가 있는지 확인한다(O)
# 3번 조합 경우의 수 = 1번 조합 경우의 수 (사칙연산) 2번 조합 경우의 수

def solution(N, number):
    possible_set = [0, [N]]
    
    if N == number: # N과 number가 같다면 그 자체로 만들 수 있음
        return 1    
    
    for i in range(2, 9): # 사용횟수의 최솟값
        case_set = []
        base_num = int(str(N)*i)
        case_set.append(base_num)
        for j in range(1, i//2+1):
            for x in possible_set[j]:
                for y in possible_set[i-j]:
                    case_set.append(x+y)
                    case_set.append(x-y)
                    case_set.append(y-x)
                    case_set.append(x*y)
                    if y != 0:
                        case_set.append(x//y)
                    if x != 0:
                        case_set.append(y//x)

            print(possible_set, case_set)
            
            if number in case_set:
                return i

            possible_set.append(case_set)
    
    return -1   # 사용횟수의 최솟값이 8을 넘으면 -1 반환


print(solution(5, 12))  # 4
#print(solution(2, 11))  # 3
#print(solution(5, 31168))   # -1