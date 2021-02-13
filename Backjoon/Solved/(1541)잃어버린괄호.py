from itertools import permutations

arr = input()
op = []     # 연산자를 저장할 리스트
nums, num = [], []

for i in list(arr):
    if i.isdigit():
        # 숫자라면 추가 
        num.append(i)
    else:
        # 연산자라면 추가
        op.append(i)
        # 여태까지 모은 자릿수를 숫자로 변환
        nums.append(int("".join(num)))
        num.clear() # 초기화
    
nums.append(int("".join(num)))

# 연산자의 시작 순서를 바꿔가면서 계산
min_value = int(129)
for i in len(op):
    value = nums[0]
    

