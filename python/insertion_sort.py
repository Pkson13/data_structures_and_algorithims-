list = [1,3,4,5,2,6]
# [1,3,4,5,5,6]
# i=0
for i in range(1,len(list)):
    now = list[i]
    j=i-1
    while j>=0 and  now < list[j]:
        list[j + 1] = list[j]
        j-=1
    list[j + 1] = now

print(list)

# tmp = 0
# i=0
# #This shit is messed up i dont know what am diong here😂 stima zikirudi do some research on insertion and selection sort
# while i < len(list):
#     if i == 0:
#         tmp = list[0]
#         i+=1
#         continue
#     if list[i] >= tmp:
#         list[i -1] = list[i]
#         tmp = list[i]
#         i+=1
#         continue
#     i+=1

# print(list)


    