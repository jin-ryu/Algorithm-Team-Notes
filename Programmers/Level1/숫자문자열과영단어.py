def solution(s):
    numbers = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' :  '4',
        'five' : '5', 
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }
    
    for key in numbers.keys():
        s = s.replace(key, numbers[key])
            
    return int(s)