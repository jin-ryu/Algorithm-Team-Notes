from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque([])
    
    for city in cities:
        # 대소문자 구분 없앰
        city = city.lower()
        
        if city in cache:
            # cache hit
            answer += 1
            # 가장 최근에 사용한 것읕 캐시 맨 끝으로 이동
            cache.remove(city)
            cache.append(city)
        else:
            # cache miss
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city)
            elif cache:
                # LRU 교체
                cache.popleft()
                cache.append(city)
                
                
                
    return answer