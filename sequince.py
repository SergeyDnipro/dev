def position_in_seq(integer):
    for count in range(1, integer):
        for elem in range(count, count + 3):
            if elem == integer:
                l1.append(elem)
                print(l1)
                return len(l1)
            else:
                l1.append(elem)


k = 10
i = 1
l1 = []

# while i != k:
#     for el in range(i, i + 3):
#         if el == k:
#             l1.append(el)
#             break
#         else:
#             l1.append(el)
#     i += 1
# print(l1)
# print(l1.index(4) + 1)

print(position_in_seq(4))
