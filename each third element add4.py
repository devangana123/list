# x=[1,2,5,3,6,5,7,8,7,5,7,2]
# i=0
# b=[]
# count=1
# while i<len(x) and count<=len(x):
#     if count==0:
#         b.append(x[i])
#     elif count%3==0:
#         x[i]=4
#         b.append(x[i])
#     else:
#         b.append(x[i])
#     count+=1
#     i+=1
# print(b) 






# a=[1,2,3,4,5,6,7,8,9,10]
# i=0
# sum=0
# multy=1
# while i<len(a):
#     if i<5 :
#         sum+=a[i]
#     else :
#         multy=multy*a[i]
#     i=i+1
# print("sum=",sum)
# print("multyply=",multy)


x=[1,2,5,3,6,5,7,8,7,5,7,2]
i=0
b=[]
count=1
while i<len(x):
    if count%3==0:
        x[i]=4
        b.append(x[i])
    else:
        b.append(x[i])
    count+=1
    i+=1
print(b) 

