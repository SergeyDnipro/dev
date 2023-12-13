import string


def check_string(string_value):
    final_list = []
    string_to_list = list(string_value)
    letter_count = 0
    # print(len(string_value))
    while letter_count < len(string_value) - 1  and len(final_list) < 100:
        letter = string_value[letter_count]
        if letter.isalpha() and letter not in forbidden_list:
            final_list.append(letter)
        letter_count += 1
        print(letter)
        print(final_list)
        print(len(final_list))


# print(string.ascii_letters)
letters_list = string.ascii_letters
forbidden_list = ['m', 'M', 'n', 'N']
check_string('abVBCdefmM_()+NNNnnnafdgdgdfgd ft5tg 45yt y dtrhg dfhd hsfdgssrtbs5y s5y  th strh g sgrg grs rgre tg sgtr gtsr grgr grgs rgr ges5t65trsdg fzg dxg se56 5ygdx fgy5d hfthrt h ezt54 ye 5yxdgbfh dyj dtrh th txh dh yuj dyjcft cjyjh gfj yfuj rdth jh xdfg xrt6sdf xd rgrtrtertdjfyukjdgzafre')
