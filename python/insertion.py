arry = [4, 5, 3, 2, 6, 3, 2, 1]

for i in range(1, len(arry)):
    # tmp = i
    min = arry[i]
    j = i - 1
    while j >= 0 and arry[j] > min:
        arry[j + 1] = arry[j]
        j -= 1
    arry[j + 1] = min
print(arry)
