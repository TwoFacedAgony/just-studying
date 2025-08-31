def unite_sorted_arrays(list_1, list_2):
    pointer_1, pointer_2 = 0, 0
    result = []

    while pointer_1 < len(list_1) and pointer_2 < len(list_2):
        if list_1[pointer_1] < list_2[pointer_2]:
            result.append(list_1[pointer_1])
            pointer_1 += 1
        else:
            result.append(list_2[pointer_2])
            pointer_2 += 1

    result += list_1[pointer_1:]
    result += list_2[pointer_2:]
    return result
