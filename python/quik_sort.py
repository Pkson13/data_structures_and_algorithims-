arry = [7, 4, 3, 2, 4, 2, 1, 5, 11, 20, 30, 29, 25, 15]


def quicksort(arry, start, end):
    if end <= start:
        return
    # pivot = len(arry)
    i = start - 1
    # print(pivot, arry[pivot - 1])
    for j in range(start, end):
        if arry[j] < arry[end]:
            i += 1
            temp = arry[i]
            arry[i] = arry[j]
            arry[j] = temp
    i += 1
    tmp = arry[end]
    arry[end] = arry[i]
    arry[i] = tmp
    quicksort(arry, start, i - 1)
    quicksort(arry, i + 1, end)


quicksort(arry, 0, len(arry) - 1)
for k in range(len(arry)):
    print(arry[k])
