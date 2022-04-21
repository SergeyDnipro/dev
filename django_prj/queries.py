Items.objects.all().order_by('group_id') # Вывод всех записей в таблице Items с сортировкой по ключу (по возрастанию даты)

Items.objects.filter(group_id='2022-04-17') # Вывод записей, связанных с датой из таблицы ToDo_date

Items.objects.create(group_id='2022-04-18', name='Feed the cat', order=Items.Order.common, stat=Items.Status.na)
# Создание записи в таблице Items

Items.objects.filter(name='Feed the cat') # Вывод всех записей по ключу 'name'

Items.objects.filter(group_id__gt='2022-04-15') # Вывод записей после какойто даты.

Items.objects.filter(id=17).update(stat='Done') # Изменение поля 'stat' - Статуса задания

Items.objects.filter(id=17).update(group_id='2022-04-18') # Изменение поля 'group_id'. запись теперь относится к другой
 # записи в таблице дат ToDo_date

Items.objects.filter(Q(stat=Items.Status.done) & Q(group_id__gt='2022-04-15')).count() # Сколько заданий имеют статус
# "сделано" после какойто даты

Items.objects.filter(name='Feed the cat').order_by('group_id') # Вывод всех записей с полем 'name', с сортировкой по дате

Items.objects.filter(Q(group_id='2022-04-17') & Q(name='Feed the cat')).update(stat=Items.Status.in_process) # Изменение
# поля 'stat', зная дату и название занятия.
