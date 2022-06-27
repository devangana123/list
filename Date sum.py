n=input("enter the date")
print(list(n))
i=0
b=[]
while i<len(n):
    if n[i]!="/":
        b.append(n[i])
    i=i+1
print(b)
i=0
sum=0
while i<len(b):
    c=int(b[i])
    sum=sum+c
    i=i+1
print(sum)