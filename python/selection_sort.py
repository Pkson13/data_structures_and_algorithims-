arry = [9, 7, 4, 2, 8, 6]
arry = [42, 7, 19, 3, 88, 55, 23, 14, 67, 2, 90, 31, 76, 8, 50]

for i in range(len(arry)):
    min = i
    for j in range(i, len(arry)):
        if arry[j] < arry[min]:
            min = j

    tmp = arry[i]
    arry[i] = arry[min]
    arry[min] = tmp
print(arry)
