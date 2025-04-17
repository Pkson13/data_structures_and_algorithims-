def merge_sort(arry :list):
    if len(arry) <= 1:
        return arry
    mid = len(arry)//2
    left_half = arry[:mid]
    right_half = arry[mid:]
    left_arry = merge_sort(left_half)
    right_arry = merge_sort(right_half)
    return merge(left_arry, right_arry)

def merge(left, right):
    # print("start merge")
    new_arry = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_arry.append(left[i])
            i += 1
        else:
            new_arry.append(right[j])
            j += 1
        
    while i < len(left):
        new_arry.append(left[i])
        i += 1

    while j < len(right):
        new_arry.append(right[j])
        j+=1

    return new_arry
listp = [25,68,43,2,4,1,4,7,89,9,99,100]
print(merge_sort(listp))
# print(listp)
# listp.sort()
# print(listp)
