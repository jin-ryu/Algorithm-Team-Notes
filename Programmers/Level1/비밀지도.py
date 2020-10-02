# 벽부분을 1, 공백부분을 0으로 부호화
def solution(n, arr1, arr2):
    answer = []

    for index in range(n):
        # or 연산을 한 후 2진수로 변환하고 n의 크기만큼 맞춤
        code = format(arr1[index] | arr2[index], "b").rjust(n, '0')   # rjust() 대신 zfill(n)도 가능
        map_line = ""

        # code에 따라 지도를 만듦
        for index2 in range(n):       
            if code[index2] == "1":
                map_line += "#"
            else:
                map_line += " "

        answer.append(map_line)

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))    
# ["#####","# # #", "### #", "# ##", "#####"]

print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))   
# ["######", "### #", "## ##", " #### ", " #####", "### # "]