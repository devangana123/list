a=[1,-2,3,-4,5,-6,7,]
i=0
b=[]
while i<len(a):
    if a[i]<0:
        b.append(0)
    else:
        b.append(a[i])
    i=i+1
print(b)