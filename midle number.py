a=[1,2,3,4,5,6,7,4,8,9]
b=[]
c=[]
i=0
while i<len(a):
    if a[i]%2==0:
        b.append(a[i])
    else:
        c.append(a[i])
    i+=1
print("even",b)
print("odd",c)
print(b[len(b)//2])
print(c[len(c)//2])


