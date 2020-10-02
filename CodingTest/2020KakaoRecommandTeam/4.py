import functools

def mergeIntervals(intervals):
    if not intervals:
        return [[0, 1]]
    answer = [intervals[0]]
    for i in range(1, len(intervals)):
        current = intervals[i]
        prev = answer[-1]
        if prev[1] > current[0]:
            prev[1] = max(current[1], prev[1])
        else:
            answer.append(current)
    return answer

def prison(n, m, h, v):
    # Write your code here
    if h == 0 and v == 0:
        return 1
        
    h.sort()
    v.sort()
    h_intervals = [[bar - 1, bar + 1] for bar in h if bar != 0] if h != 0 else []
    v_intervals = [[bar - 1, bar + 1] for bar in v if bar != 0] if v != 0 else []

    h_intervals = mergeIntervals(h_intervals)
    print(h_intervals)
    v_intervals = mergeIntervals(v_intervals)
    print(v_intervals)
    h_max = functools.reduce(lambda old, interval: max(old, interval[1] - interval[0]), h_intervals, 1)
    v_max= functools.reduce(lambda old, interval: max(old, interval[1] - interval[0]), v_intervals, 1)

    return v_max * h_max

n=6
m=6
h=[4]
v=[2]
print(prison(n, m, h, v))