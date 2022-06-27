a=[1,2,4,7,7,5,8,9,9,4,6,8]
i=0
b=[]
while i<len(a)-1:
    b.append(a[i+1]-a[i])
    i=i+1
print(b)


# a=[1,2,4,7,7,5,8,9,9,4,6,8]
# i=0
# n=[]
# while i<len(a):
#     if a[i]!=0:
#         a[i]=1
#         n.append(1)
#     i=i+1
# print(n)