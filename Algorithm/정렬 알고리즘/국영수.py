# PyPy3로 해야 맞을 수 있음
n = int(input())
students =[]
for i in range(n):
    # 학생 정보 튜플로 저장
    name, kor, eng, math = input().split()
    students.append((name, int(kor), int(eng), int(math)))

# 국어 점수 내림차순
# 영어 점수 오름차순
# 수학 점수 내림차순
# 이름 사전순
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in range(n):
    print(students[i][0])