a=[2,4,8,9,4,5,1]
i=0
while i<len(a):
    j=0
    while j<len(a)-1:
        if a[i]<a[j]:
            c=a[i]
            a[i]=a[j]
            a[j]=c
        j=j+1
    i=i+1
print(a)


# a=[2,4,8,9,4,5,1]
# i=0
# while i<len(a):               #ascending
#     j=0
#     while j<len(a)-1:
#         if a[i]<a[j]:
#             c=a[i]
#             a[i]=a[j]
#             a[j]=c
#         j=j+1
#     i=i+1
# print(a)


