import math
n, m = map(int, input().split())

print(math.gcd(n, m))

# volume_list = []
#
# if n > m:
#     for volume in range(m, 0, -1):
#         if n % volume == 0 and m % volume == 0:
#             volume_list.append(volume)
#             break
# else:
#     for volume in range(n, 0, -1):
#         if n % volume == 0 and m % volume == 0:
#             volume_list.append(volume)
#             break
#
# print(volume_list)