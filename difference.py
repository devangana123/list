list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
a=[]
for i in list1:
    if i not in list2:
        a.append(i)
print(a)


# a=[19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# b=[]
# count=0
# for i in range(len(a)):
#     if (a[i] in b):
#         pass
#     else:
#         b.append(a[i])
#         count+=1
# print(b,count)

# input_list = [1, 2, 2, 5, 8, 4, 4, 8]
# a=[]
# count=0
# for i in range(len(input_list)):
#     if (input_list[i] in a):
#         pass
#     else:
#         a.append(input_list[i])
#         count+=1
# print(a,"count=",count)


# a=[19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# i=0
# b=[]
# count=0
# while i<len(a):
#     if (a[i] in b):
#         pass
#     else:
#         b.append(a[i])
#         count+=1
#     i=i+1
# print(b,"count is",count)


