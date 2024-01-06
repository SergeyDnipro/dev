import string
from random import random, shuffle, choice


def random_word(source):
    word = choice(source).capitalize()
    for _ in range(7):
        shuffle(source)
        word += choice(source)
    return word


def binary_search(list_of_names, name):
    low = 0
    high = len(list_of_names) - 1
    count = 0
    while low <= high:
        current_index = int((high + low) / 2)
        current_name = list_of_names[current_index]
        count += 1
        print(current_name)
        print(low, high, sep=' ')
        print(current_index)
        print(name < current_name)
        if name == current_name:
            print(count)
            return current_index
        elif name < current_name:
            high = current_index - 1
        else:
            low = current_index + 1


letters_arr = list(string.ascii_lowercase)

names_arr = [random_word(letters_arr) for x in range(256)]
names_arr.sort()

binary_search(names_arr, names_arr[44])
