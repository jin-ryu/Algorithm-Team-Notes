def get_rank(match):
    if match == 6:
        return 1
    elif match == 5:
        return 2
    elif match == 4:
        return 3
    elif match == 3:
        return 4
    elif match == 2:
        return 5
    else:
        return 6
    
def solution(lottos, win_nums):
    answer = []
    match = len([i for i in lottos if i in win_nums])
    zero = lottos.count(0)
    
    return [get_rank(match+zero), get_rank(match)]