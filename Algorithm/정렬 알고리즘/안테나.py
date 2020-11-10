n = int(input())
home = list(map(int, input().split()))

home.sort()

# 아이디어 정답코드 참고
# 중간에 있는 home이 최소 거리
print(home[(n-1)//2])   # 중간 인덱스는 (n-1) //2

