from math import sqrt


def find_factor(temp_n):
    return [(temp_n // i, i) for i in range(1 , int(sqrt(temp_n)) + 1) if temp_n % i == 0]


k = int(input())

for n in range(k * 2, 1000000):
    if k == 1:
        final_result = 1
        break
    res = find_factor(n)
    if len(res) == k:
        final_result = n
        break

print(final_result)

