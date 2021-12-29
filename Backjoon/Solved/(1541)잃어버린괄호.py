# 참고: 여기서 괄호를 한 개만 치라는 말은 없었다. 적절히 여러 개를 쓸 수 있다.

ex = input()
arr = ex.split('-') # '-' 기준으로 괄호 침
result = sum(list(map(int, arr[0].split('+'))))

for i in range(1, len(arr)):
    result -= sum(list(map(int, arr[i].split('+'))))

print(result)
