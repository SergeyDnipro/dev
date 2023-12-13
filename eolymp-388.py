digit = int(input())
count = 0

while digit != 1:
    if digit % 2 == 0:
        digit = digit // 2
    else:
        digit += 1
    count += 1

print(count)
