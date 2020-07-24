import math

numbers = [int(input()) for i in range(5)]

result = 1
for num in numbers:
    result *= num
    
    # if (result**0.5).is_integer():
    if math.sqrt(result) ==  int(math.sqrt(result)):
        print("found")
        break

# for문에서도 else 사용가능
else:
    print("not found")