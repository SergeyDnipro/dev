n = int(input())
summary_time = 0
temp_time = 0
list_of_buyers_and_time = [[x for x in map(int, input().split())] for y in range(n)]

# print(list_of_buyers_and_time)
flag = True
while flag:
    for element in list_of_buyers_and_time:
        if len(list_of_buyers_and_time) >=2 and element[0] + list_of_buyers_and_time[1][0] > element[1]:
            if len(list_of_buyers_and_time) >= 3 and element[0] + list_of_buyers_and_time[1][0] + list_of_buyers_and_time[2][0] > element[2] and :
                summary_time += element[2]
                del list_of_buyers_and_time[0:3]
                break
            else:
                summary_time += element[1]
                del list_of_buyers_and_time[0:2]
                break
        else:
            summary_time += element[0]
            del list_of_buyers_and_time[0]
            break
    if len(list_of_buyers_and_time) == 0:
        flag = False

print(summary_time)
