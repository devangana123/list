# n=[4, 5, 5, 5, 3, 8]
# i=0
# while i<len(n):
#     j=0
#     count=0
#     while j<len(n):
#         if n[i]==n[j]:
#             count+=1                                                                                                                                                            
#             if count>=3:
#                 a=n[count]
#         j=j+1
#     i=i+1
# print(a)

n=[1, 1, 1, 64, 23, 64, 22, 22, 22]
b=[]
i=0
while i<len(n):
    j=0
    count=0
    while j<len(n):
        if n[i]==n[j]:
            count+=1
            if count>=3:                                            
                a=n[i]          
                if a not in b:
                     b.append(a)     
        j=j+1
    i=i+1
print(b)

# a="divya"
# b=19
# print("int(a)"+str(b))
                                 


# a="kirti\n"
# a+="neha"
# print(a)

# n=[4, 6, 4, 3, 3, 4, 3, 4, 6,5,3,1,0,6]               
# a=[]
# i=0
# while i<len(n):
#     j=0
#     count=0
#     while j<len(n):
#         if n[i]==n[j]:
#             count+=1
#             if count>=3:
#                 b=n[i]
#                 if b not in a:
#                     a.append(b)
#         j=j+1
#     i=i+1
# print(a)


# num=int(input("enter the number"))
# num1=list(str(num))
# i=0
# a=[]
# while i<len(num1):
#     b=int(num1[i])**2
#     a.append(b)
#     print(a[i],end=" ")
#     if i==len(num1)-1:
#         pass
#     i=i+1
                                                          



# a=[1,2,3,4,6,9,7]
# b=[6,5,3,7,2,8,4]
# i=0
# x=[]
# while i<len(a):
#     if a[i] not in b:
#         x.append(a[i])
#     i+=1
# print(x)


 

# a=[1,2,3,4,6,9,7]
# b=[6,5,3,7,2,8,4]
# i=0
# x=[]
# while i<len(a):
#     if a[i] in b:
#         x.append(a[i])
#     i+=1
# print(x)



