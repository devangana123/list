# a_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# occurrences = a_list.count("a"),a_list.count("n"),a_list.count("t"),a_list.count("x"),a_list.count("u"),a_list.count("g")
# print(occurrences)

a_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a","p"]
i=0
b=[]
while i<len(a_list):
    j=0
    n=[]
    count=0
    while j<len(a_list):
        if a_list[i] in a_list:
            if a_list[i]==a_list[j]:
                count+=1
        j=j+1
    n.append(a_list[i])
    n.append(count) 
    if n not in b:
        b.append(n)
    i=i+1
print(b)


      
# magic_square=[
#             [8,3,4],
#             [1,5,9],
#             [6,7,2]
# ]
# r1sum=0
# r2sum=0
# r3sum=0
# i=0
# while i<len(magic_square):
#     j=0
#     s=len(magic_square[i])
#     while j<s:
#         if i==0:
#             r1sum+=magic_square[i][j]
#         elif i==1:
#             r2sum+=magic_square[i][j]
#         else:
#             r3sum+=magic_square[i][j]
#         j+=1
#     i=i+1
# print("row",r1sum)
# print("row",r2sum)
# print("row",r3sum)


# a=[1,3,[1,2,3],4,5,[6],7]
# sum1=0
# i=0
# sum2=0
# while i<len(a):
#     k=a[i]
#     if type(k)==list:
#         j=0
#         while j<len(k):
#             sum1=sum1+k[j]
#             j=j+1
#     elif type(k)==int:
#         m=k
#         sum2=sum2+m
#     i=i+1
# print(sum1+sum2)

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



# a=[[1,2,4]]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j <len(a[i]):
#         sum+=a[i][j]
#         j+=1
#     i=i+1
# print(sum)


# num=[[1,2,3],[4,5,6],[7,8]]
# i=0
# sum=0
# while i<len(num):
#     j=0
#     while j<len(num[i]):
#         sum=sum+num[i][j]
#         j=j+1
#     i=i+1
# print(sum)
