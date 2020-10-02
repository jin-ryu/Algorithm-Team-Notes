def solution(m, k):
    index = 0

    for i in range(len(m)):
        if index >= len(k): # key 문자를 전부다 찾았으면 끝냄
            break

        if m[i] ==  k[index]:   # key 문자제거
            m =  m[:i] +  m[i+1:]
            index += 1
        
    return m
    


print(solution("kkaxbycyz", "abc"))
print(solution("acbbcdc", "abc"))
print(solution("aabcb", "ab"))