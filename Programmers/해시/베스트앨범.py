def solution(genres, plays):
    answer = []
    
    playlist = {}
    for i in range(len(genres)):
        if genres[i] not in playlist.keys():
            playlist[genres[i]] = {i: plays[i]}

        else:
            playlist[genres[i]][i] = plays[i]
 
    print(playlist)

    # dictionary가 비어 있을 때까지 반복
    while playlist:
        # play 수가 가장 많은 장르를 뽑음
        g = max(playlist.keys(), key=(lambda k: sum(playlist[k].values())))
        # 해당 장르의 play한 리스트를 뽑음
        p = playlist[g]

        # 장르에 속한 곡이 하나라면, 하나의 곡만 선택
        if len(p) < 2:
            answer += list(p.keys())
        else:
            max_key = max(p.keys(), key=lambda k: p[k])
            max_value = p[max_key]
            p.pop(max_key)
            max2_key = max(p.keys(), key=lambda k: p[k])
            max2_value = p[max2_key]

            # 장르 내 재생 횟수가 같다면 고유번호가 낮은 노래를 먼저 수록
            if max_value == max2_value :  
                answer += [min(max_key, max2_key), max(max_key, max2_key)]
            else:
                answer += [max_key, max2_key]

        playlist.pop(g)

    return answer


genres = ["classic", "pop", "classic", "classic", "pop", "jazz"]
plays = [500, 600, 150, 800, 2500, 2000]
print(solution(genres, plays))