# name="naman"
# length=len(name)
# i=0
# a=[]
# while i<length-1:
#     length-=1
#     # print(name[length])
#     a.append(name[length])
#     i=i+1
# if a==name:
#     print("it is palindrom number")
# else:
#     print("it is not palindrom")


# name="nitin"
# name=input("enter anything:-")
# length=len(name)
# rev=""
# i=-1
# while i>=-length:
#     rev+=name[i]
#     i-=1
# if name==rev:
#     print("It is an palindrome",name)
# else:
#     print("It is not an palindrome",name)






# name=['abc', 'xyz', 'aba', '1221']
# length=len(name)
# i=0 
# a=[]
# while i<length:
#     length-=1
#     print(name[length])
#     a.append(name[length])
#     i=i+1
# if name:
#     pass
# print(length)



# nums=[2,7,11,15]
# list=[]
# i=0
# target=9
# while i<len(nums):
#     sum=nums[0]+nums[i]
#     list.append(i) 
#     if sum==target:
#         print(list)
#     i+=1
# print(list)

nums=[0,1,0,3,12]
list=[]
for i in nums:
    if i>0:
        list.append(i)
print(list)