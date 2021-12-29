# 참고 (시간 초과: 입출력 성능 개선, Runtime Error(Recursion Limit): 최대 Recursion 수 계산해서 제한 풀어줌)
import sys

sys.setrecursionlimit(500000)
n, m = map(int, input().split())

# 초기화
root = [0] * n
rank = [0] * n
for i in range(n):
    root[i] = i

# x의 루트 노드를 찾는다
def find(x):
    if x == root[x]:
        return x
    
    root[x] = find(root[x])   # Path Compression
    return root[x]

def is_cycle(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        # 루트가 x인 집합과 루트가 y인 집합을 합친다
        if rank[x] < rank[y]:
            root[x] = y
        else:
            root[y] = x
        # 루트가 다르므로 사이클이 형성되지 않는다
        return False
    
    # 루트가 같으면 사이클이 형성된다
    return True

for i in range(1, m+1):
    x, y = map(int, sys.stdin.readline().split())

    if is_cycle(x, y):
        # 사이클이 완성되면 차례 출력
        print(i)
        break
else:
    print(0)