source = '10010111'
final_source = '0' + source
# source_list = [int(x) for x in source]
# source_list.insert(0, 0)
# print(source_list)
final_str = ''

for ind in range(1, len(final_source)):
    if final_source[ind] != final_source[ind - 1]:
        final_str += '1'
    else:
        final_str += '0'

print(final_str)