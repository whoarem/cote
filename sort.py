from functools import reduce

# print(reduce(lambda dic, x: dic.update({x: True}) or dic, [1, 2, 3], {}))


def quicksort(a):
    if len(a):
        pivot = a[0]
        print(pivot)
        split = reduce(
            lambda split, el: (split['left'].append(
                el) if el < pivot else split['right'].append(el)) or split,
            a[1:],
            {'left': [], 'right': []}
        )
        print(split)
        return quicksort(split['left']) + [pivot] + quicksort(split['right'])
    else:
        return a


def merge(split_1, split_2):
    i, j = 0, 0
    sorted = []
    while i < len(split_1) and j < len(split_2):
        print(i, j)
        if split_1[i] < split_2[j]:
            sorted.append(split_1[i])
            i += 1
        else:
            sorted.append(split_2[j])
            j += 1

    left_over = [part[pointer:] for pointer, part in zip(
        [i, j], [split_1, split_2]) if pointer < len(part)][0]
    sorted = sorted + left_over
    return sorted


def mergesort(a):
    if len(a) <= 1:
        return a
    else:
        half = len(a)//2
        split_1, split_2 = mergesort(a[:half]), mergesort(a[half:])
        print(split_1, split_2)
        return merge(split_1, split_2)
