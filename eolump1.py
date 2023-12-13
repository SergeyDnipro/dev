button_amount = 5
button_straight = [1, 50, 3, 4, 3]
press_quantity = 16
button_sequence = [1, 2, 3, 4, 5, 1, 3, 3, 4, 5, 5, 5, 5, 5, 4, 5]

list_of_button_status = []

for i in range(button_amount):
    if button_straight[i] < button_sequence.count(button_sequence[i]):
        list_of_button_status.append(f"{i + 1} - YES")
    else:
        list_of_button_status.append(f"{i + 1} - NO")
    # response = 'yes' if button_straight[i - 1] < button_sequence.count(i) else 'no'
    # list_of_button_status.append(response)

print(*list_of_button_status, sep='\n')

# for elem in enumerate(list_of_button_status, 1):
#     print(*elem)

# print(list_of_quantity_pressed_buttons)