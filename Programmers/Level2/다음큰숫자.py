def solution(n):
    # 2진수로 변환 (문자열 형태)
    n_list = bin(n)
    # 접두사와 숫자 제거
    prefix = n_list[:2]
    n_list = n_list[2:]
    
    flag = False
    index = 0
    for i in range(len(n_list)-1, 0, -1):
        # 끝에서 부터 1이 발견된 이후에 가장 먼저 발견된 0을 찾음
        # 그 위치에 1을 옮기고 나머지 1을 가장 최소값을 갖게함
        if n_list[i] == '1':
            flag = True
        elif flag:
            index = i
            break
    else:
        # 0이 발견되지 않는다면 자리수를 하나 증가
        count = n_list.count('1') - 1
        bin_answer = prefix + '1' + '0'*(len(n_list)-count) + '1'*count
        # 10진수로 변환
        return int(bin_answer, 2)

    length = len(n_list[index+2:])
    count = n_list[index+2:].count('1')
    bin_answer = prefix + n_list[:index] + '10' + '0'*(length-count) + '1'*count
    # 10진수로 변환
    return int(bin_answer, 2)

print(solution(78))