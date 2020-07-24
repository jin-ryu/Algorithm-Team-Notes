import collections

my_str = input().strip()
my_list = collections.Counter(sorted(my_str)).most_common()

answer = ''
for i in range(len(my_list)):
    if my_list[0][1] == my_list[i][1]:
        answer += my_list[i][0]

print(answer)