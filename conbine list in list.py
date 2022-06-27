list1=[['D','i','v','y','a'],['i','s'],['b','e','s','t']]
i=0
sum=" "
while i<len(list1):
    j=0
    while j<len(list1[i]):
        sum=sum+list1[i][j]
        j=j+1
    i=i+1
print(sum)
# conbine list in list


# num=int(input("enter the number:-"))
# if num>1:
#     print(num,"*",1,"=",num*1)
#     print(num,"*",2,"=",num*2)
#     print(num,"*",3,"=",num*3)
#     print(num,"*",4,"=",num*4)
#     print(num,"*",5,"=",num*5)
#     print(num,"*",6,"=",num*6)
#     print(num,"*",7,"=",num*7)
#     print(num,"*",8,"=",num*8)
#     print(num,"*",9,"=",num*9)
#     print(num,"*",10,"=",num*10)
# else:
#     print(num)

# list1=['D','i','v','y','a','i','s','b','e','s','t']
# i=0
# sum=" "
# while i<len(list1):
#     sum=sum+list1[i]
#     i=i+1
# print(sum)

# a=[1,0,6,0,3,0,3,6,3]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i]==0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i+=1
# print(c+b)