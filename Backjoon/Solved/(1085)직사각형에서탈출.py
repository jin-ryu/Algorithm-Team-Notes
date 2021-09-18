x, y, w, h = map(int, input().split())

# 경계선까지의 최솟값 출력
print(min(abs(x-0), abs(y-0), abs(x-w), abs(y-h)))