def merge(left, right):
    newarray = []
    i =0 
    j=0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            newarray.append(left[i])
            i+=1
        
        else:
            newarray.append(right[j])
            j+=1
    while i < len(left):
        newarray.append(left[i])
        i += 1

    while j < len(right):
        newarray.append(right[j])
        j+=1
    return newarray

def merge_sort(list):
    print(list.__len__())
    # print(len(list))
    len = list.__len__()
    if len <= 1:
        return list 
    mid = len //2

    lefthalf = list[:mid]
    righthalf = list[mid:]
    print(f"{lefthalf}\n")
    print(righthalf)
    left = merge_sort(lefthalf)
    right = merge_sort(righthalf)
    return merge(left, right)

list = [25,68,43,2,4,1,4,7,89,9,99,100]
print(merge_sort(list))