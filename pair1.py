# c=[1,2,3,4,5,6,7,8]
# i=0
# final=[]
# b=[]
# count=0
# while i<len(a):
#     if count==2:
#         final.append(b)
#         b=[]
#         count=1
#     else:
#         count+=1
#     b.append(a[i])
#     i+=1
# final.append(b) 
# print(final)


list=[10.11,12,13,14,15,16,17,18]
a=[]
i=0
k=1
while i<len(list):
    b=[list[i],list[k]]
    a.append(b)
    k=k+2
    i+=2
print(a)


# a="anisha"
# i=1
# b=[]
# while i<len(a):
#     b.append(a[-i])
#     i+=1
# print(b)



# a=[12,13,14,15]
# i=0
# d=1
# sum=0
# while i<len(a):
#     c=a[i]+[i]
#     sum=sum+c
#     i+=1
# print(sum)