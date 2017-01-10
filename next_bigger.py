import itertools

def next_bigger(num):
    digit_list = list(str(num))

    in_order = True
    i = -1

    while in_order and i >= -len(digit_list):
        # print(digit_list[i:])
        if digit_list[i:] != sorted(digit_list[i:], reverse=True):
            in_order = False
            perm_start_index = i

        i -= 1

    if in_order == True:
        return -1

    candidate_list = list(itertools.permutations(digit_list[perm_start_index:]))
    candidate_list = [''.join(lst) for lst in candidate_list]

    prefix = ''.join(digit_list[:perm_start_index])
    num_list = sorted(list(set([int(prefix + x) for x in candidate_list])))

    current_index = num_list.index(num)

    return num_list[current_index + 1]