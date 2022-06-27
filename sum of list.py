a=[12,13,34,546,67,34,67,98,46]
i=0
sum=0
while i<len(a):
    b=str(a[i])
    j=0
    while j<len(b):
        sum=sum+int(b[j])
        j=j+1
    i=i+1
    print(sum)


# a=[12,13,34,546,67,34,67,98,46]
# s=0
# i=0
# r=0
# while i<len(a):
#     d=a[i]
#     while d>0:
#         r=d%10
#         s=s+r
#         d=d//10
#     i=i+1
#     print(d)

# a=[[2,2,3,7],[5,7,9],[4,5,7],5,6,7]
# sum=0
# for i in a:
#     if type(i)==list:
#         for j in i:
#             sum=sum+j
#     else:
#         sum=sum+i
# print(sum)