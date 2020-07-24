s,n = input().strip().split()
n = int(n)

print(s.ljust(n))       # 좌측 정렬
print(s.center(n))      # 가운데 정렬
print(s.rjust(n))       # 우측 정렬