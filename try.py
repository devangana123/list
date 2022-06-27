# a=[4,4,2,8]
# b=[2,6,8,5]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+a[i]+b[i]
#     i=i+1
# print(sum)

    
# # First second digit==2:

# num=input("enter the number:-")
# a=len(num)-1
# b= int(num)//10**a 
# c=b%10
# if c==2:
#     print("yes")
# else:
#     print("no")

# x=[1,2,5,3,6,5,7,8,7,5,7,2]
# i=0
# b=[]
# c=x.index[i]
# while i<len(x):
#     if c%2!=0:
#         b.append(x[i])
#     i=i+1
# print(b)

# i=2
# while i<len(x):
#     if x[i]==4:
#         i=i+3
# print(x[i])
    
# a=[10000,2000,3000,500,700]
# i=0
# b=[]
# while i<len(a):
#     c=str(a[i])
#     b.append(int(c[0]))
#     i=i+1
# print(b)

#1 2 3 4
#5 6 7 8
#9 10 11 12
#13 14 15 16

# a=[1,2,4,5,3,2,3,4,2,3,6,7,8,5]
# i=0
# l=[]
# while i<len(a):
#     j=0
#     count=0
#     while j<len(a):
#         if (a[i])==a[j]:
#             count+=1
#         j=j+1
#     if count==1:
#         l.append(a[i])
#     i=i+1
# print(l)


# a=[12,13,34,546,67,34,67,98,46]
# i=0
# sum=0
# while i<len(a):
#     b=str(a[i])
#     j=0
#     while j<len(b):
#         sum=sum+int(b[j])
#         j=j+1
#     i=i+1
#     print(sum)



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

# a=[[2,2,3,7],[5,7,9],[4,5,7]]
# i=0 
# while i<len(a):
#     max=0
#     j=0
#     while j<len(a[i]):
#         if (a[i][j])>max:
#             max=a[i][j]
#         j=j+1
#     i=i+1
#     print(max)
# i=0
# while i<len(a):
#     max1=0
#     j=0
#     while j<len(a[i]):
#         if (a[i][j])>max1:
#             if a[i][j]!=max:
#                 max1=a[i][j]
#         j=j+1
# #     i=i+1
# #     print("second max",max1)


# a=[[2,2,3,7],[5,7,9],[4,5,7]]
# s=0
# while s<len(a):
#     i=0 
#     max=0
#     while i<len(a[s]):
#         if (a[s][i])>max:
#             max=a[s][i]
#         i=i+1
#     print("max",max)
#     i=0
#     secondmax=0
#     while i<len(a[s]):
#             if (a[s][i])>secondmax:
#                 if a[s][i]!=max:
#                     secondmax=a[s][i]
#             i=i+1
#     print("second max",secondmax)
#     s+=1

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

# a=[[2,2,3,7],[5,7,9],[4,5,7],5,6,7]
# sum=0
# for i in a:
#     if type(i)==list:
#         for j in i:
#             sum=sum+j
#     else:
#         sum=sum+i
# print(sum)


# a=[-21,-34,-86,-1,-57,-5,-67,-7,-6]
# i=0
# max1=a[0]
# while i<len(a):
#     if a[i]>max1:
#         max1=a[i]
#     i=i+1
# print("greater number",max1)
# i=0
# max2=a[0]
# while i<len(a):
#     if a[i]>max2:
#         if a[i]!=max1:
#             max2=a[i]
#     i+=1
# print("second greate",max2)
# i=0
# max3=a[0]
# while i<len(a):
#     if a[i]>max3:
#         if a[i]!=max1 and a[i]!=max2:
#             max3=a[i]
#     i+=1
# print("third greater",max3)


# a=[-21,-34,-86,-1,-57,-5,-67,-7,-6]
# i=0
# max1=a[0]
# while i<len(a):
#     if a[i]>max1:
#         max1=a[i]
#     i=i+1
# print("greater number",max1)
# i=0
# max2=a[0]
# while i<len(a):
#     if a[i]>max2:
#         if a[i]!=max1:
#             max2=a[i]
#     i+=1
# print("second greate",max2)
# i=0
# max3=a[0]
# while i<len(a):
#     if a[i]>max3:
#         if a[i]!=max1 and a[i]!=max2:
#             max3=a[i]
#     i+=1
# print("third greater",max3)

# a=input("enter anything:-")
# if a>="a" and a<="z":
#     print("it is the letters")
# elif a=="@" or a=="$" or a=="#":
#     print("it is the special character")
# else:
#     print("it is the number")



# a=[[2,2,3,7],[5,7,9],[4,5,7],5,6,7]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             sum=sum+a[i][j]
#             j+=1
#     else:
#         sum=sum+a[i]
#     i+=1
# print(sum)


# a=[[2,2,3,7],[5,7,9],[4,5,7]]
# s=0
# while s<len(a):
#     i=0 
#     max=0
#     while i<len(a[s]):
#         if (a[s][i])>max:
#             max=a[s][i]
#         i=i+1
#     s+=1
#     print("max",max)



# a=[[2,2,3,7],[5,7,9],[4,7,5]]
# i=0 
# while i<len(a):
#     max=0
#     j=0
#     while j<len(a[i]):
#         if (a[i][j])>max:
#             max=a[i][j]
#         j=j+1
#     i=i+1
#     print(max)

# a=[1,2,3,4,5,6,7,4,8,9]
# b=[]
# c=[]
# i=0
# while i<len(a):
#     if a[i]%2==0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i+=1
# print("even",b)
# print("odd",c)
# print(b[len(b)//2])
# print(c[len(c)//2])

# i=1
# sum=0
# while i<=10:
#     a=int(input("enter the number:-"))
#     sum=sum+a
#     i+=1
# print(sum)



# a=[[7,9,3,4],[6,3,2,9]]
# sum2=0
# sum1=0
# i=0
# while i< len(a):
#     j=0
#     while j<len(a[i]):
#         if j==0:
#             sum1+=a[j][i]
#         else:
#             sum2+=a[j][i]
#         j=j+1
#     i=i+1
# print("sum",sum1)
# print("sum",sum2)



# a=[[7,9,3,4],[6,3,2,9]]
# sum1=0
# sum2=0
# i=0
# b=[]
# while i< len(a):
#     j=0
#     while j<len(a[i]):
#         if i==0:
#             sum1+=a[j][i]
#             b.append(sum1)
#             # print(sum1)
#         elif i==1:
#             sum2+=a[j][i]
#             # print(sum2)
#             b.append(sum2)
#         j=j+1
#     i=i+1
# print(b)




# sum=0
# i=1
# while i<=11:
#     num=int(input("enter the number:-"))
#     sum+=num
#     avg=sum/i
#     i+=1
# print(avg)

# list=[2,7,2,8,3,7,9,5,8,3,4]
# l=[]
# odd=1
# i=0
# while i<=len(list):
#     if odd%2!=0:
#         l.append(list[i])
#     odd+=1
#     i+=1
# print(l)


# num=[1,3,8,9,4,3,6,5,8,9,5,6,2,1]
# i=0
# even_sum=0
# odd_sum=0
# even=[]
# odd=[]
# while i<len(num):
#     if num[i]%2==0:
#         even.append(num[i])
#         even_sum+=num[i]
#     else:
#         odd.append(num[i])
#         odd_sum+=num[i]
#     i+=1
# print("even number",even)
# print("odd number",odd)
# print("sum of even number",even_sum)
# print("sum of even number",odd_sum)

# str=input("enter the number")
# i=1
# str1=[]
# while i<=len(str):
#     str1.append(str[-i])
#     i+=1
# print(str1)


# list=[1,2,3,4,7,9,6,4,3,3,9,2,5,7,5]
# count=1
# i=0
# a=[]
# while i<len(list):
#     if count%3==0:
#         # list[i]=4
#         a.append(4)
#     else:
#         a.append(list[i])
#     count+=1
#     i+=1
# print(a)

