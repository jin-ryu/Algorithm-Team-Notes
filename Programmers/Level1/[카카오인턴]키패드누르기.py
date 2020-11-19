def solution(numbers, hand):
    answer = ''
    keypad = {1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5:(1,1), 6: (1,2), 7: (2,0), 8: (2,1), 9: (2,2), "*":(3,0), 0: (3,1), "#": (3,2)}
    left = keypad["*"]
    right = keypad["#"]  
    
    for i in range(len(numbers)):
        # 주의 : numbers[i] == 1 or 4 or 7은 불가능
        if numbers[i] ==  1 or numbers[i] ==  4 or numbers[i] == 7:
            answer += 'L'
            left = keypad[numbers[i]]
              
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            answer += 'R'
            right = keypad[numbers[i]]
              
        else:
              location =  keypad[numbers[i]]
              left_dist = abs(location[0]-left[0]) + abs(location[1]-left[1])
              right_dist = abs(location[0]-right[0]) + abs(location[1]-right[1])
              
              if left_dist == right_dist and hand == "right" or right_dist < left_dist:
                    answer += 'R'
                    right = keypad[numbers[i]]
              elif left_dist == right_dist and hand == "left" or right_dist > left_dist:
                    answer += 'L'
                    left = keypad[numbers[i]]
            
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))	# LRLLLRLLRRL
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))	# LRLLRRLLLRR
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))	# LLRLLRLLRL