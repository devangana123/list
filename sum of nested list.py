# a=[1,3,[1,2,3],4,5,[6],7]
# sum1=0
# i=0
# sum2=0
# while i<len(a):
#     k=a[i]
#     if type(k)==list:
#         j=0
#         while j<len(k):
#             sum1=sum1+k[j]
#             j=j+1
#     elif type(k)==int:
#         m=k
#         sum2=sum2+m
#     i=i+1
# print(sum1+sum2)


# a=[[2,2,3,7],[5,7,9],[4,5,7],5,6,7]
# sum1=0
# i=0
# sum2=0
# while i<len(a):
#     k=a[i]
#     if type(k)==list:
#         j=0
#         while j<len(k):
#             sum1=sum1+k[j]
#             j=j+1
#     elif type(k)==int:
#         m=k
#         sum2=sum2+m
#     i=i+1
# print(sum1+sum2)

lists=[[1,2,3],[3,2,1][2,3,4,5,6]]
list2=[]

for i in lists:
    sum=0
    for j in i:
        sum+=j
    list2.append(sum)
for s in list2:
    for n in list2:
        if s==n:
            print(s)
        elif s>n:
            print(s)
            

# a=[[2,2,3,7],[5,7,9],[4,5,7],5,6,7]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         for j in a[i]:
#             sum=sum+j
#     else:
#         sum=sum+a[i]
#     i=i+1
# print(sum)


# a=[[2,2,3,7],[5,7,9],[4,5,7],[5,6,7]]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         for j in a[i]:
#             sum=sum+j
#             avg=sum/len(a[i])
#     i=i+1
# print("sum",sum,"avg",avg)



