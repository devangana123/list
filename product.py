a=[[1,2,3],[4,5,6,7,8,9],[1,2,3,6],[7,8,9,6,7]]
i=0
max=0
while i<len(a):
    if len(a[i])>max:
        max=len(a[i])
        s=a[i]
        j=0
        sum=0
        p=0
        while j<len(s):
            sum=sum+(s[j])
            p=p*s[j]
            p+=1
            j=j+1
    i=i+1
print("max of the list:",s)
print("sum of the max list:",sum)
print("product of list:",p)