def update_dictionary(d, key, value):

    if key in d.keys():
        d[key].append(value)
    elif 2*key in d.keys():
        d[2*key].append(value)
    else:
        d[2*key] = [value]
        
    return

d = {}
print(update_dictionary(d, 1, -1))

print(d)
update_dictionary(d, 0, 0)
print(d)
update_dictionary(d, 101, -30)
print(d)
update_dictionary(d, 101, -0)
print(d)
update_dictionary(d, 2, 55)
print(d)         
update_dictionary(d, 0, 8)
print(d)
update_dictionary(d, 1, 7)
print(d)
update_dictionary(d, 202, 5)
print(d)
update_dictionary(d, 3, 65)
print(d)
