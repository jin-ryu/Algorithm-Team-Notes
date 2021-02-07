import re
from itertools import product

def solution(user_id, banned_id):
    answer = set()
    candidates = []
    
    for ban in banned_id:
        # 정규식에 맞게 변환  (* -> .)
        ban = ban.replace("*", ".")
        p = re.compile(ban)
        
        c = []
        for user in user_id:
            match = p.match(user)
            if len(ban) == len(user) and match:
                # 정규식과 매치되는 아이디 모음
                # match 함수는 정규식과 맞는지만 체크, 완전히 동일한지 확인하려면 길이도 확인해야 함
                c.append(user)
                
        # 매치되는 리스트 추가
        candidates.append(c)
        
    result = list(product(*candidates))
    for r in result:
        # 중복되는 경우 제거
        if len(r) == len(set(r)):
            answer.add(tuple(sorted(r)))
            
    return len(answer)