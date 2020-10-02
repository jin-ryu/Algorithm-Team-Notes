import collections

def countDuplicate(numbers):
    # Write your code here
    counter = collections.Counter(numbers).most_common()
    count = 0
    for c in counter:
        if c[1] != 1:
            count+=1
    return count

numbers = [1,3,3,4,4,4]
print(countDuplicate(numbers))