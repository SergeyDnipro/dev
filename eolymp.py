test_number = input('Нмер теста:')
number_of_tasks = int(input('количество заданий:'))
list_of_tasks = []
final_list = []
f_list = []

for task in range(1, number_of_tasks + 1):
    start, stop = map(int, input('enter time:').split())
    set_temp = set(range(start, stop + 1))
    list_of_tasks.append(set_temp)

for task_id in range(len(list_of_tasks)):
    f_list.append(task_id + 1)
    for task_id2 in range(task_id + 1, len(list_of_tasks)):
        if not list_of_tasks[task_id].isdisjoint(list_of_tasks[task_id2]):
            f_list.append(task_id2 + 1)
            
    final_list.append(f_list)
    f_list = []


print(list_of_tasks)
print(final_list)