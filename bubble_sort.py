def bubble_sort(array : list):
    for i in range(len(array) - 1):
        print("w")
        for j in range(len(array) - i - 1):
            print("q")
            if array[j] > array[j + 1]:
                tmp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = tmp
    return array

print(bubble_sort([3,4,1,2]))