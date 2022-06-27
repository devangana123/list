marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]
i=0
k=1
while i<len(marks):
    j=0
    sum=0
    while j<len(marks[i]):
        sum=sum+marks[i][j]
        j=j+1
        avg=sum/len(marks[i])
    print("average of",k,"year",avg)
    i=i+1
    k+=1


# a=[1,2,3,4,5,6]
# a[1:3]=[7]
# print(a)

# a=[1,2,3,4,5,6]
# a.pop()
# print(a)

