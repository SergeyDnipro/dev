import math

while True:
    try:
        n = int(input())
        dividers = []
        value = n
        # k = int(math.sqrt(value))

        while value != 1 and value > 0:
            k = int(math.sqrt(value))
            for divider in range(2, k + 3):
                if value % divider == 0:
                    dividers.append(divider)
                    value = value // divider
                    break
                if divider == k + 2:
                    dividers.append(value)
                    value = 1
                    break

        counter = 1
        str_temp = ''

        for element in range(1, len(dividers)):
            if dividers[element - 1] == dividers[element]:
                counter += 1
                if element + 1 == len(dividers):
                    str_temp += f"{dividers[element]}^{counter}"
            elif element + 1 == len(dividers) and len(dividers) != 2:
                str_temp += f"{dividers[element - 1]}^{counter}*{dividers[element]}" if counter > 1 else f"{dividers[element - 1]}*{dividers[element]}"
            elif len(dividers) == 2 and element + 1 == len(dividers):
                str_temp += f"{dividers[element - 1]}*{dividers[element]}"
            else:
                str_temp += f"{dividers[element - 1]}^{counter}*" if counter > 1 else f"{dividers[element - 1]}*"
                counter = 1
        if len(dividers) == 1:
            str_temp += f"{dividers[0]}"
        if n == 1:
            str_temp += f"{n}"
        if n == 0:
            str_temp += f"{n}"
        print(str_temp)
    except:
        break
