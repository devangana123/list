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
#         sum=sum+magic_square[i][col]
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
#     print(sum1,"row"
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
#             print("it is not magic square")
#     else:
#         print("it is not magic square")
# else:
#     print("it is not magic square")


#  magic_square = [
# [8, 3, 4],
# [1, 5, 9],
# [6, 7, 2] 
# ]
# i=0
# row_sum=0
# while i<len(magic_square):
#     j=0
#     while j<len(magic_square):
#         row_sum=row_sum+magic_square[j][i]
#         j=j+1
#     i=i+1
#     print(row_sum)
#     # print()
# i=0
# colum_sum=0
# while i<len(magic_square):
#     j=0
#     while j<len(magic_square):
#         colum_sum=colum_sum+magic_square[j][i]
#         j=j+1
#     i=i+1
#     print(colum_sum)
#     # print()
# i=0
# left_diagonal=0
# while i<len(magic_square):
#     j=0
#     while j<len(magic_square):
#         left_diagonal=left_diagonal+magic_square[j][i]
#         j=j+1
#     i=i+1
#     print(left_diagonal)
#     # print()
# i=0
# right_diagonal=0
# while i<len(magic_square):
#     j=0
#     while j<len(magic_square):
#         right_diagonal=right_diagonal+magic_square[j][i]
#         j=j+1
#     i=i+1
#     print(right_diagonal)
#     # print()
# if row_sum==colum_sum==left_diagonal==right_diagonal:
#     print("it is magic square",row_sum,colum_sum,left_diagonal,right_diagonal)
# else:
#     print("it is not magic square",row_sum,colum_sum,left_diagonal,right_diagonal)
    



magic_square = [[8, 3, 4],
                [1, 5, 9],
                [6, 7, 2]]
row1=0
row2=0
row3=0
i=0
while i< len(magic_square):
    j=0
    while j<len(magic_square[i]):
        if i==0:
            row1+=magic_square[i][j]
        elif i==1:
            row2+=magic_square[i][j]
        elif i==2:
            row3+=magic_square[i][j]
        j=j+1
    i=i+1
print("row1 :",row1)
print("row2 :",row2)
print("row3 :",row3)
column1=0
column2=0
column3=0
i=0
while i< len(magic_square):
    j=0
    while j<len(magic_square[i]):
        if i==0:
            column1+=magic_square[j][i]
            # print(magic_square[j][i])
        elif i==1:
            column2+=magic_square[j][i]
        elif i==2:
            column3+=magic_square[j][i]
        j=j+1
    i=i+1

print("column1 :",column1)
print("column2 :",column2)
print("column3 :",column3)
leftdiagonal=0
rightdiagonal=0
i=0
while i< len(magic_square):
    j=0
    while j<len(magic_square[i]):
        if i==j:
            leftdiagonal=leftdiagonal+magic_square[i][j]
        if i+j==len(magic_square[i])-1:
            rightdiagonal=rightdiagonal+magic_square[i][j]
        j=j+1
    i=i+1
print("leftdiagonal :",leftdiagonal)
print("rightdiagonal :",rightdiagonal)
if column1==column2==column3==leftdiagonal==rightdiagonal==row1==row2==row3:
    print("It as an magic square.")
else:
    print("It is not an magic square.")



