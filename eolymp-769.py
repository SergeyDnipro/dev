# result = [dict(zip('xy', [int(elem) for elem in input().split()])) for loop_iter in range(3)]
new_coord = []
x_coords = []
y_coords = []

# for _ in range(3):
#     temp_result = input().split()
#     x_coords.append(int(temp_result[0]))
#     y_coords.append(int(temp_result[1]))

for x_temp in x_coords:
    new_coord.append(x_temp) if x_coords.count(x_temp) == 1 else None
for y_temp in y_coords:
    new_coord.append(y_temp) if y_coords.count(y_temp) == 1 else None


print(*new_coord, sep=' ')