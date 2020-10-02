# dfs, bfs 둘다 상관없는데, bfs가 더 개념적으로 맞는듯
from collections import deque

def solution(begin, target, words):
    graph = {}
    N = len(words)

    if target not in words:
        return 0        # 타겟 단어가 없는 경우 변환 불가

    # 그래프 딕셔너리로 생성
    words.append(begin)
    for i in range(N+1):
        graph[words[i]] = []
        for j in range(N):
            if i==j:
                continue
            if isOneLetterDifferent(words[i], words[j]):
                graph[words[i]].append(words[j]) 

   
    return dfs(graph, begin, target, words)

"""
def bfs(graph, begin, target, words):
    need_visit = deque([])
    need_visit.append((begin, 0))

    while need_visit:
        node, level = need_visit.popleft()
        
        if level > len(words):  # 모든 단어를 다 탐색해도 없으면 0
            return 0
        
        for n in graph[node]:
            if n == target:  
                return level+1  # 그때 level을 반환
            need_visit.append((n, level+1)) # 다음 노드와 level을 튜플로 추가

    return 0

"""
def dfs(graph, begin, target, words):
    visited = []
    need_visit = [begin]

    while need_visit:
        node = need_visit.pop()
        while node not in visited:
            if node == target:
                return len(visited)
            visited.append(node)
            need_visit.extend(graph[node])
    
    return 0

# 단어의 길이는 3이상 10이하
def isOneLetterDifferent(target, word):
    count = 0
    for ch1, ch2 in zip(target, word):
        if ch1 == ch2:
            count += 1
    
    if count == len(word)-1:
        return True
    return False

print(solution("hit", "cog", ["hot", "lot", "dog", "dot", "log", "cog"] ))  # 4
#print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))    # 0