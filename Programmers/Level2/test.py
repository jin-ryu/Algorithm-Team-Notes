#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def make_group(self, goldValues):
        # 그룹 반환하는 메소드
        group = []
        sub_group = []

        for i in range(len(goldValues)):
            if goldValues[i] != 0:
                sub_group.append(goldValues[i])
            elif sub_group:
                group.append(sub_group)
                sub_group = []
        if sub_group:
            group.append(sub_group)

        # 처음값과 끝값이 둘다 있으면 이어진 그룹이므로 합쳐줌
        if len(group) >= 2 and goldValues[0] != 0 and goldValues[-1] != 0:
            group[0] = group[-1] + group[0]
            group.pop()

        # 최대로 연속된 그룹 뽑음   
        lengths = [len(g) for g in group]
        max_len = max(lengths)
        group = [group[i] for i in range(len(lengths)) if lengths[i] == max_len]
    
        return group

    def solution(self, goldValues):
        answer = 0
        turn = 0
        
        while sum(goldValues) != 0:
            group = self.make_group(goldValues)
            for i in range(len(group)):
                # 그룹에서 최대값 뽑음
                max_value = max(group[i])
                idx = goldValues.index(max_value)
                goldValues[idx] = 0
                if turn % 2 ==0:
                    answer += max_value
            # 차례 변경
            turn += 1
            

        return answer
    

a = Solution()

print(a.solution([5,2,1,4,3,1]))    #10

print(a.solution([1,2,1])) # 3
print(a.solution([2,1,4,1,2,1,8,1])) # 12

