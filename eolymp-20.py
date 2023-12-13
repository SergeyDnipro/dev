def int_to_list_of_digits(varible: int) -> int:
    return sum(map(int, str(varible)))


source = input()
source_digit = int(source)
source_list_of_digit = list(map(int, source))
new_digit_sum = sum(source_list_of_digit)
result = source_digit
count = 0

for _ in range(100000000):
    if result <= 0:
        break
    result -= new_digit_sum

    new_digit_sum = int_to_list_of_digits(result)
    count += 1
print(count)