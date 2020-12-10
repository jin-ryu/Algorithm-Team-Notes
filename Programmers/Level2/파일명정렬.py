import string

def solution(files):
    answer = []
    
    for i in range(len(files)):
        # head, number, tail 분할
        head = ""
        number = ""
        tail = ""
        for j in range(len(files[i])):
            if files[i][j] in string.digits:
                # 숫자이면 number에 추가
                number += files[i][j]
            else:
                if number:
                    # 숫자가 아닌데 number가 이미 존재
                    # tail 완성 시키고 종료
                    tail = files[i][j:]
                else:
                    # 숫자가 아닌데 number가 아직 비어있다면 head
                    head += files[i][j]
        # 리스트에 추가
        answer.append((head, number, i))
    return answer