a=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
i=0
final=[]
b=[]
count=0
while i<len(a):
    if count==3:
        final.append(b)
        b=[]
        count=1
    else:
        count+=1
    b.append(a[i])
    i+=1
final.append(b) 
print(final)
list=[10.11,12,13,14,15,16,17,18]


# a=[]
# i=0
# k=1
# while i<len(list):
#     b=[list[i],list[k]]
#     a.append(b)
#     k=k+2
#     i+=2
# print(a)

# a=["red","maroon","yellow","olve"]
# b=a.splite()
# print(b)