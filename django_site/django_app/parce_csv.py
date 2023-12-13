with open('airport-codes_csv.csv', 'r', encoding='utf-8') as file:
    # data = file.readline().strip().split(';')
    # print(data)
    # data = file.readline().split(';')
    # print(data)
    # print(data)
    # print(file.readlines())

    result = [element.strip().split(';')[2] for element in file.readlines() if element.strip().split(';')[5] == 'UA']
    # res = sorted(result)
    # result.sort()
print(f"{sorted(result)}")
print(len(result))
