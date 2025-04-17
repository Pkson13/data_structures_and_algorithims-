list = []
# num = 0

for i in range(1, 100):
    list.append(i)
print(list)

# list2 = []
# for j in range(0, 50):
#     list2.append(list[j])

# print(list2)
num = 0
def recursivebinarysearch(list, target, first=0, last=None, num=0):
    # first = 0
    # last = len(list) - 1
    if last is None:
        last = len(list) - 1
    if len(list) == 0:
        print("not found")
        return False
    
    num = num + 1
    print(num)    
    mid = (first + last)//2
    if list[mid] == target:
        return mid
    elif list[mid] < target:
        first = mid + 1
        return(recursivebinarysearch(list, target, first, last, num ))
    else:
        last = mid - 1
        return(recursivebinarysearch(list, target, first, last, num ))
    
print(recursivebinarysearch(list, 75))