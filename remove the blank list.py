a=[5, 6, [], 3, [], [], 9]
i=0
k=[]
while i<len(a):
    if a[i]!=[]:
        k.append(a[i])
    i=i+1
print(k)