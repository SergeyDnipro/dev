result = []
with open('airport-codes_csv.csv', 'r', encoding='utf-8') as file:
    # print(file.readline().strip().split(';'))
    ind = file.readline().strip().split(';')
    country_index = ind.index('iso_country')
    country_name = ind.index('name')
    for line in file.readlines():
        line_res = line.strip().split(';')
        if line_res[country_index] == 'UA':
            result.append(line.replace(';', '-'))

result.sort()
print(*result, sep='\n')

with open('ukraine_airports.csv', 'w', encoding='utf-8') as destination_file:
    destination_file.writelines(result)
    destination_file.w

