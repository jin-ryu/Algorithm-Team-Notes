from itertools import combinations
from collections import Counter

class DisjointSet:
    def __init__(self, n):
        self.data = [-1 for _ in range(n)]
        self.size = n
    
    def find(self, index):	
        value = self.data[index]
       	if value < 0:
            return index
        
        return self.find(value)
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:	# 같은 그래프인 경우
            return
        
        # 더 작은 인덱스 쪽을 붙임
        if self.data[x] < self.data[y]:
            self.data[x] += self.data[y]
            self.data[y] = x
        else:
            self.data[y] += self.data[x]
            self.data[x] = y
            
        self.size -= 1
                

def solution(n, edges):
    comb = list(combinations(range(len(edges)), 2))

    for edge1, edge2 in comb:   # 조합을 돌음
        disjointset = DisjointSet(n)

        for i in range(len(edges)): # 위 조합을 제외하고 그래프 생성
            if i == edge1 or i == edge2:
                continue
            disjointset.union(edges[i][0], edges[i][1])

        trees = list(Counter(disjointset.data).values())    # 서브 트리별 노드카운트 체크
        print(Counter(disjointset.data))
        if trees == [n//3]*3:       # 서브 트리 노드수가 모두 같으면 반환
            return [edge1, edge2]


print(solution(9, [[0,2],[2,1],[2,4],[3,5],[5,4],[5,7],[7,6],[6,8]]))