number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19  ]
i=0
a=[]
while i<len(n):
    j=4
    while j<len(n):
        if (n[i]+n[j]==number):
            a.append([n[i],n[j]])
        j=j+1
    i=i+1
print(a)  