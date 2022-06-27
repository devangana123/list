num=int(input("enter the number"))
num1=list(str(num))
i=0
a=[]
while i<len(num1):
    b=int(num1[i])**2
    a.append(b)
    print(a[i],end=" ")
    i=i+1
