# a=[1,-2,3,-4,5,-6,7,]
# i=0
# b=[]
# while i<len(a):
#     if a[i]<0:
#         b.append(0)
#     else:
#         b.append(a[i])
#     i=i+1
# print(b)

# a="The Bag"
# # b=a.split()
# i=0
# c=[]
# d=[]
# while i<len(a):
#     if a[i]>="A" and a[i]<="Z":
#         c.append(a[i])
#     else:
#         d.append(a[i])
#     i+=1
# print("upper",c)
# print("lower",d)





# a=[2,4,3,6,9,34,30,12,45,9,21,15]
# i=0
# b=[]
# while i<len(a):
#     if a[i]%3==0:
#         b.append(3)
#     else:
#         b.append(a[i])
#     i=i+1
# print(b)

# list1 = [1, 2, 2, 5, 8, 4, 4, 8]
# i=0
# min=0
# while i<len(list1):
#     if list1[i]<min:
#         min=list1[i]
#     i=i+1
# print(min)    


# a=["slowball","chery","bubble","grull"]
# b=["cat","dog","fish","goat"]
# c=[1,2,2,6]
# length = len(a) 
# counter = 0
# while counter < length:
#     print([a[counter] +(b[counter])+ str(c[counter])])
#     counter+=1

# z="123abc"
# i=1
# b=[]
# while i<=len(z):
#     b.append(z[-i])
#     i=i+1
# print(b)

# a="The Quick Brow Fox"
# x=[]
# b=[]
# count=0
# count1=0
# for i in (a):
#     if i>"a" and i<"z":
#         x.append(i)
#         count+=1
#     elif i>"A" and i<"Z":
#         b.append(i)
#         count+=1
# print("small letter",x)
# print("capital letter",b)

# magic_square = [
# [8, 3, 4],
# [1, 5, 9],
# [6, 7, 2]
# ]
# i=0
# total=15
# while i<len(magic_square):
#     col=0
#     sum=0
#     s=len(magic_square[i])
#     while col<s:
#         sum=sum+magic_square[col][col]
#         col=col+1
#     print(sum,"colum")
#     a=sum+sum+sum
#     i=i+1
# print(a)
# j=0
# while j<len(magic_square):
#     row=0
#     sum1=0
#     while row<len(magic_square[j]):
#         sum1=sum1+magic_square[row][row]
#         row+=1
#     print(sum1,"row")
#     h=sum1+sum1+sum1
#     j=j+1
# print(h)
# x=magic_square[0][0]+magic_square[1][1]+magic_square[2][2]
# z=magic_square[0][2]+magic_square[1][1]+magic_square[2][0]
# if x==total:
#     if z==total:
#         c=x+z
#         print("diagonal",c)
#         if sum==sum1==total:
#             print("it is the magoic square")
#         else:
#             print("it is not magilen(magic_square[j])c square")
#     else:
#         print("it is not magic square")
# else:
# #     print("it is not magic square")
# magic_square = [
# [8, 3, 4],
# [1, 5, 9],
# [6, 7, 2]
# ]
# i=0
# total=15
# while i<len(magic_square):
#     col=0
#     sum=0
#     s=len(magic_square[i])
#     while col<s:
#         sum=sum+magic_square[col][col]
#         col=col+1
#     print(sum,"colum")
#     a=sum+sum+sum
#     i=i+1
# print(a)
# j=0
# while j<len(magic_square):
#     row=0
#     sum1=0
#     while row<len(magic_square[j]):
#         sum1=sum1+magic_square[row][row]
#         row+=1
#     print(sum1,"row")
#     h=sum1+sum1+sum1
#     j=j+1
# print(h)
# x=magic_square[0][0]+magic_square[1][1]+magic_square[2][2]
# z=magic_square[0][2]+magic_square[1][1]+magic_square[2][0]
# if x==total:
#     if z==total:
#         c=x+z
#         print("diagonal",c)
#         if sum==sum1==total:
#             print("it is the magoic square")
#         else:
#             print("it is not magilen(magic_square[j])c square")
#     else:
#         print("it is not magic square")
# else:
#     print("it is not magic square")

 
# m = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ]
# i=0
# v=15
# while i<len(m):
#     col=0
#     sum=0
#     s=len(m[i])
#     while col<s:
#         sum=sum+m[i][col]
#         col+=1
#     print(sum,"column")
#     a=sum+sum+sum
#     i+=1
# print(a)
# j=0
# while j<len(m):
#     row=0
#     sum1=0
#     while row<len(m[j]):
#         sum1=sum1+m[row][row]
#         row+=1
#     print(sum1,"row")
#     h=sum1+sum1+sum1
#     j+=1  
# print(h)
# x=m[0][0]+m[1][1]+m[2][2]
# z=m[0][2]+m[1][1]+m[2][0]
# if x==v:
#     if z==v:
#         c=x+z
#         print("diagonal:",c)
#         if sum==sum1==v:
#             print("it is magic square")
#         else:
#             print("it is not magic square")
#     else:
#         print("it is not magic square")
# else:
#     print("it is not magic square")

# list1=[['D','i','v','y','a'],['i','s'],['b','e','s','t']]
# i=0
# sum=" "
# while i<len(list1):
#     j=0
#     while j<len(list1[i]):
#         sum=sum+list1[i][j]
#         j=j+1
#     i=i+1
# print(sum)

# print(4.2 or 2 or 2)

# print(3.2//3//5+6%3+4//2 and 1)

# print((2+3//4-(3**3) and 4) or 6)

# print(not(8 or 3 and 4*3) or 6)


# print((not 1) and (not 2) and (not 3))

# print(not(0 and  9 and 6**4 and 9 and 5))

# a=[1,2,3,4,]
# b=[10,20,30,40]
# i=0
# p=-1
# while i<len(a):
#     print([a[i],b[p]])
#     p=p-1
#     i=i+1     
 

# a=[1,2,3,4,]
# b=[10,20,30,40]
# i=0
# p=-1
# while i<len(a):
#     print([a[i],b[p]])
#     p=p-1
#     i=i+1   

# a=[1,2,"a1",3,"b2","11"]
# # i=0
# b=[]
# while i<len(a):
#     if type(a[i])==int:
#        b.append(a[i])
#     i=i+1
# print(b)


# a=[[1,2],[3,4],[5],[8,9]]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             b. append(a[i][j])
#             j=j+1
#     i=i+1
# print(b)


# https://docs.google.com/document/d/1lBD6ykxC8_Dvm3hFlDri4k22T6Yg4Cfybylxd2MMeHo/edit

# a=[5, 6, [], 3, [], [], 9]
# i=0
# k=[]
# while i<len(a):
#     if a[i]!=[]:
#         k.append(a[i])
#     i=i+1
# print(k)


# list1 = [2, -7, 5, -64, -14]
# i=0
# a=[]
# b=[]
# count=0
# count1=0
# while i<len(list1):
#     if list1[i]>0:
#         a.append(list1[i])
#         count+=1
#     else:
#         b.append(list1[i])
#         count1+=1
#     i=i+1
# print("positive number",a,"count",count)
# print("negative number",b,"count",count1)

# num=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]


# a=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
# b=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]

# # You will be given a number and you need to return it as a string in Expanded Form. For example:
# 12  # Should return '10 + 2'
# 42 # Should return '40 + 2'
# 70304  # Should return '70000 + 300 + 4'

# a="divya"
# print(tuple(a))

# string="72314"
# final=""
# i=0
# while i<len(string):
#     final+=string[i]
#     j=1
#     while j<=(len(string)-(i+1)):
#         final+="0"
#         j+=1
#     if i == (len(string)-1):
#         break                                                 
#     else:
#         final+="+"
#     i+=1
# print(final)



# string=input("enter the number")
# final=""
# i=0
# while i<len(string):
#     final+=string[i]
#     j=1
#     while j<=(len(string)-(i+1)):
#         final+="0"
#         j+=1
#     if i == (len(string)-1):
#         break                                                 
#     else:
#         final+="+"
#     i+=1
# print(final)

# Given start and end of a range, write a Python program to print all positive numbers in given range.
# Example:
# Input: start = -4, end = 5
# Output: 0, 1, 2, 3, 4, 5 

# a=[2,3,5,4,7,6,8,9,10]
# i=0
# b=[]
# while i<len(a):
#     x=a[i]**2
#     b.append(x)
#     i=i+1
# print(b) 



# a=[19,2,3,4,5,6,7]
# i=0
# min=a[i]
# while i<len(a):
#     if a[i]<min:
#         min=a[i]
#     i=+1
# print(min)
# i=0
# min1=a[i]
# while i<len(a):
#     if a[i]<min1:
#         a[i]=min1
#     i=+1
# print(min1)


# question_list=[
#     ["which is the capital of India ?"],
#     ["who is prime minister of India ?"],
#     ["which course teach in Navgurukul ?"]
# ]
# option=[
#     ["Goa","Karnatak","Kerla","New Delhi"],
#     ["Ramnath Kovind","Jawaharlal Nehru","Narendra Modi","Atalbihari Vajpei"],
#     ["Software Engineering","Agriculture","Science and Technologi","Medical Course"]
# ]
# ans_list=[4,3,1]
# # option_list=[
# #     ["1)Goa","4)New Delhi"],
# #     ["2)Jawaharlal Nehru","3) Narendra Modi"],
# #     ["1)Softwaere Engineering","3)Science and Technology"]
# # ]
# print("kon banega karodpati,kbc")
# i=0
# sum=0
# countt=0
# while i<len(question_list):
#     print(question_list[i])
#     a=0
#     b=i
#     while a<len(option[i]):
#         k=option[i][a]
#         print(a+1,k)
#         a=a+1
#     num1=input("do you want to use 50-50 lifeline")
#     if num1=="yes":
#         print("accepted")

# num=int(input("enter the number"))
# num1=num%10
# if num1==3:
#     print(num1)
# else:
#     print("no")

# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print(" ",end=" ")
#         b=b+1
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#     print()
#     K=1
#     while K<=i:
#         print(K,end=" ")
#         K=K+1

#     i=i+1             

# a=[[1,2,3],[4,5,6,7,8,9],[1,2,3,6],[7,8,9,6,7]]
# i=0
# max=a[i]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if a[i]>max:
#             max=a[i]
#         j=j+1
#     i=i+1
# print(max)


# a=[[1,2,3],[4,5,6,7,8,9],[1,2,3,6],[7,8,9,6,7]]
# max=0
# for i in a:
#     if len(i)>max:
#         max=len(i)
#         b=i
# # print(max)
# print(b)






# a=[[1,2,3],[4,5,6,7,8,9],[1,2,3,6],[7,8,9,6,7]]
# i=0
# max=a[i]
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#         b=i
#     i=i+1
# print(max)
# print(b)


# number=[50,40,23,70,53,12,5,10,7]
# i=0
# max=0
# while i<len(number):
#     if number[i]>max:
#         max=number[i]
#     i=i+1
# print(max)


# https://docs.google.com/spreadsheets/d/1ho-GETT-h7l3ejY-_6KEBDm09cU1eHXLwrFKvjbl4hY/edit#gid=0

# a=[1,2,3,4,5,6,7,8,9]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]==a[j]:
#             b.append(a[i])
#         j=j+1
#     i=i+1
# print(b)

# print("1")
# x=1
# i=1
# while i<=4:
#     j=1
#     while j<=i:
#         print("1""0",end=" ")
#         j=j+1
#     print(x)
#     print()
#     i=i+1

a=[1,2,3,2,2,3,1,1,4,5,3,4,5,1,2,3,4,5]
i=0
b=[]
count=0
while i<len(a):
    if a[i] in b:
        count+=1
    else:
        b.append(a[i])
    i=i+1
print(b)
print(count)


# a=[1,2,3,2,2,3,1,1,4,5,3,4,5,1,2,3,4,5]
# i=0
# b=[]
# while i<len(a):
#     if a[i] in b:
#         pass
#     else:
#         b.append(a[i])
#     j=0
#     count=0
#     while j<len(a):
#         if a[i]==a[j]:           
#             count+=1
#         j=j+1
#     print(a[i],count)
#     i=i+1
# print(b)

# d="my name is divya nilu kiran"
# i=0
# count=0
# while i<len(d):
#     if d[i]==" ":
#         count+=1
#     i=i+1
# print(count)

# a=[[1,2,3],[4,5,6,7,8,9],[1,2,3,6],[7,8,9,6,7]]
# max=0
# for i in a:
#     if len(i)>max:
#         max=len(i)
#         b=i
#         # sum=sum+b[i]
# print(b)

# a=[[1,2,3],[4,5,6,7,8,9],[1,2,3,6],[7,8,9,6,7]]
# i=0
# max=0
# while i<len(a):
#     if len(a[i])>max:
#         max=len(a[i])
#         s=a[i]
#     i=i+1
# print(s)
# j=0
# s=0
# sum=0
# while j<len(s):
#     sum=sum+s[j]
#     j=j+1
# print(sum)

# a=[[1,2,3],[4,5,6,7,8,9],[1,2,3,6],[7,8,9,6,7]]
# i=0
# max=0
# while i<len(a):
#     if len(a[i])>max:
#         max=len(a[i])
#         s=a[i]
#         j=0
#         sum=0
#         p=0
#         while j<len(s):
#             sum=sum+(s[j])
#             p=p*s[j]
#             p+=1
#             j=j+1
#     i=i+1
# print("max of the list:",s,p)
# print("sum of the max list:",sum)
# print("product of list:",p)

# num=int(input("enter the number"))
# while num>0:
#     k=num%10
#     num=num//10
#     if k==0:
#         print("zero")
#     elif k==1:
#         print("one")
#     elif k==2:
#         print("two")
#     elif k==3:
#         print("three")
#     elif k==4:
#         print("four")
#     elif k==5:
#         print("five")
#     elif k==6:
#         print("six")
#     elif k==7:
#         print("seven")
#     elif k==8:
#         print("eight")
#     elif k==9:
#         print("nine")

# a=["zero","one","two","three","four","five","six","seven","eight","nine"]
# b=int(input("enter the number:"))
# i=0
# while i<len(a):
#     if i==b:
#         print(a[i])
#     i=i+1
