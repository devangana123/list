# name=["divya","sweety","nilu","kiran"]
# i=0
# while i<4:
#     print("wellcome",name[i])
#     i=i+1

# name=["divya",16,"sweety",16,"nilu",11,"kiran",14]
# append=name[0]=15
# print(name[0])

# name=["divya",16,"sweety",16,"nilu",11,"kiran",14]
# # # print(len[name])

# student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
# list_length = len(student_marks)
# index = 0
# less_than50 = 0
# more_than50 = 0
# while index < list_length:
#     marks = student_marks[index]
#     if marks < 50:
#         less_than50 = less_than50 + 1
#     else:
#         more_than50 = more_than50 + 1
#     index = index + 1
# print ("Marks more than 50: " + str(more_than50))
# print ("Marks less than 50: " + str(less_than50))


# student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
# print(len(student_marks))

# student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
# b=len(student_marks)
# print("length of the list",b)

# student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
# b=max(student_marks)
# print(b)

# student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
# b=min(student_marks)
# print(b)


# a=["divya","kiran","nilu","lalita","sakshi","sweety"]
# b=len(a)
# print(b)

# a=[12,32,43,54,65,67,87,98,90,0]
# append=a=56
# print(a)

# a="nav"
# a+="gurukul"
# print(a)

# a=22("house")
# b=a*3
# print(b)

# binary=[0,1,0,1,0,1,0,1]
# a=0
# c=0
# for i in range(-1,-(len(binary)+1),-1):
# 	b=binary[i]
# 	if b==1:
# 		c+=2**a
# 	a+=1
# print("Bianry to Decimal is :- ",c)

# d=int(input("enter the number"))
# a=[]
# for j in range (d):
# 	e=int(input())
# 	a.append(e)
# 	c=0
# 	b=0
# for i in range(-1,-len(a)-1,-1):
# 	 c=a[i]*2*b+c
# 	 b+=1
# print(c)


# decimal = int(input("Enter number which you want to convert: "))
# num = ""
# while decimal != 0:
# 	num = str(decimal % 2) + num
# 	decimal //= 2
# print(num)


# # Negative indexing in lists
# my_list = ['p','r','o','b','e']
# # last item
# print(my_list[-1])
# # fifth last item
# print(my_list[-5])


# # List slicing in Python
# my_list = ['p','r','o','g','r','a','m','i','z']
# # elements from index 2 to index 4
# print(my_list[2:5])
# # elements from index 5 to end
# print(my_list[5:])
# # elements beginning to end
# print(my_list[:])

# Correcting mistake values in a list
# odd = [2, 4, 6, 8]
# # change the 1st item    
# odd[0] = 1            
# print(odd)
# # change 2nd to 4th items
# odd[1:4] = [3, 5, 7]  
# print(odd)

# odd = [2, 4, 6, 8,8,4,3,]
# print(odd[::-2])

# a=[12,34,56,13,19,8]
# # a1=(a[:])
# # print(a1)
# a1=(a[5:-5:-1])
# print(a1)

# a=[19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# b=[]
# count=0
# for i in range(len(a)):
#     if (a[i] in b):
#         pass
#     else:
#         b.append(a[i])
#         count+=1
# print(b,count)


# number=[23,14,56,12,19,9,15,25,31,42,43]
# i=0
# sum=0
# a=[]
# b=[]
# while i<len(number):
#     sum=sum+number[i]
#     if number[i]%2==0:
#         a.append(number[i])
#     else:
#         b.append(number[i])
#     i=i+1
# print("sum of the list:-",sum)
# print("even number:-",a)
# print("odd number",b)
# sum1=0
# i=0
# while i<len(a):
#     sum1=sum1+(a[i])
#     i=i+1
# print("sum of even number",sum1)
# sum2=0
# i=0
# while i<len(b):
#     sum2=sum2+(b[i])
#     i=i+1
# print("sum of odd number",sum2)

# name=input("enter the letters")
# length=len(name)
# rev=""
# i=-1
# while (i>=-length):
#     rev+=name[i]
#     i-=1
# if  rev==name:
#     print("it is palendrom",name)
# else:
#     print("it is not palendrom",name)

# number=[50,40,23,70,53,12,5,10,7]
# i=0
# max=0
# while i<len(number)-1:
#     if number[i]>max:
#         max=number[i]
#     i=i+1
# print(max)


# a=["python",12,1.7,True]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==str:
#         b.append(a[i])
#     i=i+1
# print(b)

# a=[1,2,3,4,5,6]
# print(a[:4])

# n=int(input("enter the number"))
# a=n%10
# b=(a*10)
# c=n//10
# d=b+c
# print(d)

# magic_square = [
# [8, 3, 4],
# [1, 5, 9],
# [6, 7, 2]
# ]
# print (type(magic_square))
# print (type(magic_square[0]))
# print (type(magic_square[1]))
# print (sum(magic_square[0]))
# print (sum(magic_square[1]))
# print (sum(magic_square[2]))
