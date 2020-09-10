def solution(a, b):
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    # 2016년은 윤년이므로 2월은 29일
    dates = [31, 29, 31, 30, 31, 30, 31, 31, 30, 30, 31, 30, 31]

    # 1월 1일이 금요일이므로 일수에 +4해줌
    # 전체 일수 = a월 이전의 일수 + b일 + 4 
    return days[(sum(dates[:a-1]) + b + 4) % 7]


a = 5
b = 24
print(solution(a,b))