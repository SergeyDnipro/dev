queue_of_customers = []
service_list = []
flag = True

while flag:
    result = input().split()
    if int(result[0]) == 0:
        break
    elif int(result[0]) == 1:
        operation, client_id, priority_number = map(int, result)
        # for item in queue_of_customers:
        #     if priority_number == item[1]:
        #         del queue_of_customers[queue_of_customers.index(item)]
        #         break
        #     if client_id == item[0]:
        #         del queue_of_customers[queue_of_customers.index(item)]
        #         break
        queue_of_customers.append((client_id, priority_number))
    queue_of_customers.sort(key=lambda x: x[1], reverse=True)
    if queue_of_customers:
        if int(result[0]) == 2:
            service_list.append(queue_of_customers[0][0])
            del queue_of_customers[0]
        elif int(result[0]) == 3:
            service_list.append(queue_of_customers[-1][0])
            del queue_of_customers[-1]
    else:
        service_list.append(0)
print(*service_list, sep='\n')
