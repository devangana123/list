a=[1,2,"a1",3,"b2","11"]
i=0
b=[]
while i<len(a):
    if type(a[i])==int:
       b.append(a[i])
    i=i+1
print(b)