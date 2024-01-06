a = 640
b = 1680
count = []


# def find_biggest_side(a, b):
#     short_side, long_side = (a, b) if a < b else (b, a)
#     if long_side % short_side == 0:
#         return short_side
#     return find_biggest_side(short_side, long_side % short_side)
#
#
# print(find_biggest_side(a, b))

# for side in range(1, a + 1):
#     if a % side == 0 and b % side == 0:
#         count.append([side, (a // side) * (b // side)])
#
# print(count)

arr = [199, 2, 4, 0, 10, 14, 16, 3, 6, 17]


# def find_sum(source):
#     if len(source) == 0:
#         return 0
#     return source.pop() + find_sum(source)
#
#
# print(sum(arr))
# print(find_sum(arr))

def q_sort(source):
    if len(source) < 2:
        return source
    base_element = source[len(source) // 2]
    less_arr = [x for x in source if x < base_element]
    greater_arr = [x for x in source if x > base_element]
    return q_sort(less_arr) + [base_element] + q_sort(greater_arr)

print(q_sort(arr))
