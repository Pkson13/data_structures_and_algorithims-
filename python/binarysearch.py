def binarysearch(list, target):
    start = 0
    end = len(list) - 1
    num = 0
    while start <= end:
        # mid = (start + end)/2 
        mid2 = (start + end)//2 
        num += 1
        if list[mid2] == target:
            return mid2, num
        elif list[mid2] > target:
            end = mid2 - 1
        else:
            start = mid2 + 1

    
list = []
# num = 0

for i in range(1, 100000):
    list.append(i)
print(list)

# print(binarysearch(list, 61, num))
# print(num)
(mid2, num) = binarysearch(list, 99999)
print(mid2, num)

def recursivebinarysearch(list, target, first=0, last=None):
    # first = 0
    # last = len(list) - 1
    if last is None:
        last = len(list) - 1
    
    mid = (first + last)//2
    if list[mid] == target:
        return mid
    elif list[mid] < target:
        first = mid + 1
        return(recursivebinarysearch(list, target, first, last ))
    else:
        last = mid - 1
        return(recursivebinarysearch(list, target, first, last ))
    
print(recursivebinarysearch(list, 99999))