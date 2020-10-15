def magicIndex(array: list) -> int:
    return magicIndex(array, 0 , len(array)-1)


def magicIndex(array:list, int start, int end) -> int:
    if end > middle:
        return -1
    middle = (array[start] + array[end])/2
    if array[middle] == middle:
        return middle
    elif array[middle] < middle:
        return magicIndex(array, middle, end)
    elif array[middle] > middle:
        return magicIndex(array, start, middle)
